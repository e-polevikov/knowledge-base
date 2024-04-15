import sys

class Node:
    def __init__(self):
        self.symbol = None
        self.left = None
        self.right = None


def decode_tree(encoded_tree):
    def traverse(node):
        nonlocal idx

        if idx >= len(encoded_tree):
            return

        if encoded_tree[idx] == '0':
            node.left = Node()
            idx += 1
            traverse(node.left)

            node.right = Node()
            idx += 1
            traverse(node.right)
        else:
            symbol = chr(int(encoded_tree[idx + 1 : idx + 1 + 16], 2))
            node.symbol = symbol
            idx += 16

    def _traverse(node, code):
        if node.symbol is not None:
            print(node.symbol, code)
        else:
            _traverse(node.left, code + '0')
            _traverse(node.right, code + '1')

    tree_root, idx = Node(), 0

    traverse(tree_root)
    
    return tree_root


if __name__ == "__main__":
    filename = sys.argv[1]
    data = None

    with open(filename, "br") as f:
        data = f.read().strip()
    
    encoded_tree_size = int.from_bytes(data[:2], byteorder=sys.byteorder)
    encoded_tree = ''.join(map(lambda byte: '{0:08b}'.format(byte), data[2 : encoded_tree_size + 2]))

    tree_root = decode_tree(encoded_tree)

    encoded_text_size = int.from_bytes(
        data[encoded_tree_size + 2 : encoded_tree_size + 2 + 8],
        byteorder=sys.byteorder
    )

    byte_idx = 2 + encoded_tree_size + 8
    num_decoded_symbols = 0
    curr_node = tree_root

    output_filename = filename.split('.')[0] + "_copy.txt"

    with open(output_filename, "x") as f:
        while num_decoded_symbols < encoded_text_size:
            curr_byte = data[byte_idx]
            bits = '{0:08b}'.format(curr_byte)

            for bit in bits:
                if bit == '1':
                    curr_node = curr_node.right
                else:
                    curr_node = curr_node.left

                if curr_node.symbol is not None:
                    f.write(curr_node.symbol)
                    num_decoded_symbols += 1
                    curr_node = tree_root

                    if num_decoded_symbols == encoded_text_size:
                        break

            byte_idx += 1
