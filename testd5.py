class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return None

    def front(self):
        if not self.is_empty():
            return self.queue[0]
        return None

    def size(self):
        return len(self.queue)

    def __str__(self):
        return str(self.queue)


# Пример использования очереди:
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print("Очередь:", queue)
print("Первый элемент:", queue.front())
print("Удалённый элемент:", queue.dequeue())
print("Очередь после удаления:", queue)
