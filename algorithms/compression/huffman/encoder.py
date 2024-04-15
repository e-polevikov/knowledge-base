import sys
import matplotlib.pyplot as plt
import heapq
from collections import Counter


def plot_symbols_counts(symbols_by_counts, plot_title):
    symbols = list(map(lambda item: item[0], symbols_by_counts))
    counts = list(map(lambda item: item[1], symbols_by_counts))

    _, axes = plt.subplots()

    axes.bar(symbols, counts)
    axes.set_ylim((0, 1.01 * counts[0]))
    axes.set_ylabel("Symbol count")
    axes.set_xlabel("Symbol")
    axes.set_title(f"{plot_title}, Symbols by counts")

    plt.show()


class Node:
    def __init__(self, symbol, count, left, right):
        self.symbol = symbol
        self.count = count
        self.left = left
        self.right = right
    
    def __lt__(self, other):
        return self.count < other.count

    def __str__(self):
        return f"{self.symbol}: {self.count}"


def build_prefix_codes(symbols_by_counts):
    nodes = list(map(
        lambda item: Node(
            symbol=item[0],
            count=item[1],
            left=None,
            right=None),
        symbols_by_counts)
    )

    heapq.heapify(nodes)

    while len(nodes) > 1:
        node1 = heapq.heappop(nodes)
        node2 = heapq.heappop(nodes)

        heapq.heappush(nodes,
            Node(
                symbol=None,
                count=node1.count + node2.count,
                left=node1,
                right=node2
            )
        )
    
    def traverse(node, code):
        if node.symbol is not None:
            codes[node.symbol] = code
        else:
            traverse(node.left, code + '0')
            traverse(node.right, code + '1')

    tree_root = nodes[0]
    codes = dict()
    traverse(tree_root, '')

    return tree_root, codes


def encode_tree(tree_root, filename):
    def traverse(node):
        if node.symbol is not None:
            encoded_tree.append('1')
            encoded_tree.append('{0:016b}'.format(ord(node.symbol)))
        else:
            encoded_tree.append('0')
            traverse(node.left)
            traverse(node.right)


    encoded_tree = []

    traverse(tree_root)

    encoded_tree = ''.join(encoded_tree)
    encoded_tree += '0' * (8 - len(encoded_tree) % 8)
    encoded_tree_size = len(encoded_tree) // 8

    with open(filename, "bx") as f:
        f.write(encoded_tree_size.to_bytes(length=2, byteorder=sys.byteorder))

        for i in range(0, len(encoded_tree), 8):
            bits = encoded_tree[i : i + 8]
            byte = int(bits, 2).to_bytes(length=1, byteorder=sys.byteorder)
            f.write(byte)


def encode_text(text, codes, filename):
    text_size = len(text)
    encoded_text = ''

    with open(filename, "ab") as f:
        f.write(text_size.to_bytes(length=8, byteorder=sys.byteorder))

        for symbol in text:
            encoded_text += codes[symbol]

            if len(encoded_text) >= 8 * 10:
                for i in range(0, len(encoded_text), 8):
                    start, end = i, i + 8

                    if end > len(encoded_text):
                        break
                    else:
                        bits = encoded_text[start : end]
                        byte = int(bits, 2).to_bytes(length=1, byteorder=sys.byteorder)
                        f.write(byte)

                encoded_text = encoded_text[len(encoded_text) - len(encoded_text) % 8:]
        
        if len(encoded_text) > 0:
            encoded_text += '0' * (8 - len(encoded_text) % 8)

            for i in range(0, len(encoded_text), 8):
                start, end = i, i + 8
                bits = encoded_text[start : end]
                byte = int(bits, 2).to_bytes(length=1, byteorder=sys.byteorder)
                f.write(byte)


if __name__ == "__main__":
    filename = sys.argv[1]
    text = ""

    with open(filename) as f:
        text = f.read().strip()
    
    symbols_by_counts = Counter(text).most_common()

    plot_symbols_counts(
        symbols_by_counts=symbols_by_counts,
        plot_title=filename
    )

    tree_root, codes = build_prefix_codes(symbols_by_counts)

    output_filename = filename.split('.')[0] + ".bin"

    encode_tree(tree_root, output_filename)
    encode_text(text, codes, output_filename)
