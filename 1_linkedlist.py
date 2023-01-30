class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def printList(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        return True

    def appendList(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1

        if self.length == 1:
            self.head = None
            self.tail = None
        return temp.value

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length = 0
        if self.length == 0:
            self.tail = None
        return temp.value

    def get_index(self, index):
        if index >= self.length or index < 0:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, value):
        temp = self.get_index(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert_value(self, index, value):
        if index >= self.length or index < 0:
            return None
        if index == 0:
            self.prepend(value)
            return True
        if index == self.length:
            self.appendList(value)
            return True
        new_node = Node(value)
        temp = self.get_index(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    def remove(self, index):
        if index >= self.length or index < 0:
            return None
        if index == 0:
            self.pop_first()
            return True
        if index == self.length:
            self.pop()
            return True
        previous = self.get_index(index - 1)
        temp = previous.next
        previous.next = temp.next
        temp.next = None
        self.length -= 1
        return True

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        before = None
        # print(after.value)
        # return True
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after


obj = LinkedList(1)
obj.appendList(2)
obj.appendList(3)
obj.appendList(4)
# obj.appendList(12)
# print(obj.get_index(2).value)
# obj.set_value(3, 87)
# print(obj.pop_first())
#obj.insert_value(3, 54)
# obj.remove(1)
obj.reverse()
obj.printList()
