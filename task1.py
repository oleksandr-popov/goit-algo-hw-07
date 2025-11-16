import random

from core.avltree import *

def get_min_value_node(node):
    current = node
    while current.left is not None:
        current = current.left
    return current


if __name__ == "__main__":
    root = None
    keys = [random.randint(-100, 100) for _ in range(15)]

    for key in keys:
        root = insert(root, key)

    print("AVL-Дерево:")
    print(root)

    print("Список значень:", sorted(keys))
    print("Мінімальне значення у дереві:", get_min_value_node(root).key)
