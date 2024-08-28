class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # Вставка нового узла
        if value < self.value:
            if self.left is None:
                self.left = TreeNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = TreeNode(value)
            else:
                self.right.insert(value)

    def search(self, value):
        # Поиск узла по значению
        if self.value == value:
            return True
        elif value < self.value and self.left:
            return self.left.search(value)
        elif value > self.value and self.right:
            return self.right.search(value)
        return False

    def in_order_traversal(self):
        # Симметричный обход дерева (left, root, right)
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()
        elements.append(self.value)
        if self.right:
            elements += self.right.in_order_traversal()
        return elements


# Пример использования бинарного дерева:
root = TreeNode(10)
root.insert(5)
root.insert(20)
root.insert(3)
root.insert(7)

print("Симметричный обход дерева:", root.in_order_traversal())
print("Поиск 7:", root.search(7))
print("Поиск 15:", root.search(15))
