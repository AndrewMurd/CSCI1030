#Andrew Murdoch
#CSCI 1030U
#Lab9
#2018-11-26


class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
    
    def __str__(self):
        return self.items.__str__()
        
    
    
queue = Queue()
print('isEmpty():', queue.isEmpty())
print('empty:', queue)
queue.enqueue(10)
print('after enqueue(10):', queue)
print('isEmpty():', queue.isEmpty())
queue.enqueue(1)
print('after enqueue(1):', queue)
print('dequeue():', queue.dequeue())
print('after dequeue():', queue)
queue.enqueue(2)
print('after enqueue(2):', queue)
queue.enqueue(3)
print('after enqueue(3):', queue)
queue.enqueue(4)
print('after enqueue(4):', queue)
print('dequeue():', queue.dequeue())
print('after dequeue():', queue)
print('dequeue():', queue.dequeue())
print('after dequeue():', queue)
print('dequeue():', queue.dequeue())
print('after dequeue():', queue)
print('dequeue():', queue.dequeue())
print('after dequeue():', queue)
print('isEmpty():', queue.isEmpty())