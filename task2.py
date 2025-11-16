import random

from core.avltree import *

def get_max_value_node(node):
    current = node
    while current.right is not None:
        current = current.right
    return current


if __name__ == "__main__":
    root = None
    keys = [random.randint(-100, 100) for _ in range(15)]

    for key in keys:
        root = insert(root, key)

    print("AVL-Дерево:")
    print(root)

    print("Список значень:", sorted(keys))
    print("Максимальне значення у дереві:", get_max_value_node(root).key)
