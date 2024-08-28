class Queue:
   def __init__(self):
       self.items = []

   def is_empty(self):
       return self.items == []

   def enqueue(self, item):
       # Добавляем элемент в конец очереди
       self.items.append(item)

   def dequeue(self):
       # Удаляем элемент из начала очереди
       if not self.is_empty():
           return self.items.pop(0)
       return None

   def size(self):
       return len(self.items)

# Пример использования очереди:
queue = Queue()

print(queue.is_empty())

queue.enqueue("действие 1")
queue.enqueue("действие 2")
queue.enqueue("действие 3")
queue.enqueue("действие 4")

print(queue.is_empty())
print(queue.size())

print(queue.dequeue())
print(queue.size())
