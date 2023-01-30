class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.line = 1

    def print(self):
        if self.line == 0:
            return None
        temp = self.first
        while(temp):
            print(temp.value)
            temp = temp.next
        return True

    def enqueue(self, value):
        new_node = Node(value)
        if self.line == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.line += 1
        return True

    def dequeue(self):
        if self.line == 0:
            return None
        if self.line == 1:
            self.first = None
            self.last = None
        else:
            temp = self.first
            self.first = self.first.next
            temp.next = None
            temp = None
        self.line -= 1
        return True


obj = Queue(2)
obj.enqueue(3)
obj.enqueue(4)
obj.dequeue()
obj.print()
