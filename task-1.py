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

    def find_max(self):
        if not self.root:
            return None

        current = self.root
        while current.right:
            current = current.right
        return current.key

if __name__ == "__main__":
    bst = BinarySearchTree()

    values = [10, 5, 15, 3, 7, 12, 18]
    for value in values:
        bst.insert(value)

    max_value = bst.find_max()
    print(f"Максимальне значення у дереві: {max_value}")