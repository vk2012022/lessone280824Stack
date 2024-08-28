class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return None

    def size(self):
        return len(self.stack)

    def __str__(self):
        return str(self.stack)


# Пример использования стека:
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print("Стек:", stack)
print("Верхний элемент:", stack.peek())
print("Удалённый элемент:", stack.pop())
print("Стек после удаления:", stack)
