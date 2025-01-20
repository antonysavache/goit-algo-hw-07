class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if not self.root:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert_recursive(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert_recursive(node.right, key)

    def sum_values(self):
        return self._sum_recursive(self.root)

    def _sum_recursive(self, node):
        if not node:
            return 0
        return node.key + self._sum_recursive(node.left) + self._sum_recursive(node.right)

if __name__ == "__main__":
    bst = BinarySearchTree()

    values = [10, 5, 15, 3, 7, 12, 18]
    for value in values:
        bst.insert(value)

    total_sum = bst.sum_values()
    print(f"Сума всіх значень у дереві: {total_sum}")