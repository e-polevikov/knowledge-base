import sys
import math
import heapq
import bitstring
from collections import Counter


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


if __name__ == "__main__":
    filename = sys.argv[1]

    input_bytes = None

    with open(filename, "rb") as f:
        input_bytes = f.read()
    '''
    bits_distributions = []
    bit7 = ""

    for _ in range(32):
        bits_distributions.append([0, 0])



    for i in range(0, len(input_bytes), 4):
        float32 = input_bytes[i:i + 4]
        float32_bits = bitstring.BitArray(float32)

        for idx, bit in enumerate(float32_bits):
            bits_distributions[idx][int(bit)] += 1
            
            if idx in [0]:
                bit7 += str(int(bit))
    '''

    bytes_by_counts = Counter(input_bytes).most_common()
    #tree_root, codes = build_prefix_codes(bytes_by_counts)

    code_length = 0
    entropy = 0.0

    for b, count in bytes_by_counts:
        print(b, count)
        prev_idx = None
    
        for i in range(len(input_bytes)):
            if input_bytes[i] == b:
                if prev_idx is None:
                    prev_idx = i
                else:
                    print(i - prev_idx, end=" ")
                    prev_idx = i
            
        print()
        #code_length += count * len(codes[b])
        #entropy += -(count / len(input_bytes)) * math.log(count / len(input_bytes))
    
    #print("Huffman code length (bytes): ", code_length / 8)
    #print("Initial num of bytes: ", len(input_bytes))
    #print("Entropy:", entropy)
    '''
    for idx, bit_counts in enumerate(bits_distributions):
        bit_counts_ratio = None

        if min(bit_counts) > 0:
            bit_counts_ratio = max(bit_counts) / min(bit_counts)

        print(idx, bit_counts, bit_counts_ratio)
    
    bit7 = [bit7[i:i + 11] for i in range(0, len(bit7), 11)]
    byte7_counts = Counter(bit7).most_common()

    tree_root, codes = build_prefix_codes(byte7_counts)

    byte7_entropy = 0.0
    code_length = 0

    print(byte7_counts[:20])
    print(len(byte7_counts))

    for b, cnt in byte7_counts:
        code_length += cnt * len(codes[b])
        byte7_entropy +=- (cnt / len(bit7)) * math.log(cnt / len(bit7))

    print(byte7_entropy)
    print(code_length / 11)
    print(len(bit7))
    '''
