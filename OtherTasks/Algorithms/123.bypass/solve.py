# Решение выдает ошибку на тесте (WA id: 9)
# Я не совсем понимаю логику решения

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_recursive(node.right, value)

    def in_order_traversal(self):
        elements = []
        self._in_order_helper(self.root, elements)
        return elements

    def _in_order_helper(self, node, elements):
        if node is not None:
            self._in_order_helper(node.left, elements)
            elements.append(node.value)
            self._in_order_helper(node.right, elements)


def main():
    input_numbers = list(map(int, input().split()))
    bst = BinaryTree()

    for number in input_numbers:
        if number == 0:
            break
        bst.insert(number)

    sorted_elements = bst.in_order_traversal()
    for element in sorted_elements:
        print(element)

if __name__ == '__main__':
    main()
