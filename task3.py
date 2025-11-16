import random

from core.avltree import *

def get_sum_nodes_values(node):
    if not node:
        return 0
    return node.key + get_sum_nodes_values(node.left) + get_sum_nodes_values(node.right)


if __name__ == "__main__":
    root = None
    keys = [random.randint(-100, 100) for _ in range(15)]

    for key in keys:
        root = insert(root, key)

    print("AVL-Дерево:")
    print(root)

    print("Список значень:", sorted(keys))
    print("Сума всіх значень у дереві:", get_sum_nodes_values(root))
