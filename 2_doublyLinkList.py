class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def printList(self):
        temp = self.head
        while(temp is not None):
            print(temp.value)
            temp = temp.next
        return True

    def apppend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        self.length += 1

        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            self.head.prev = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return True

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length / 2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index >= self.length or index < 0:
            return None
        if index == 0:
            self.prepend(value)
            return True
        if index == self.length:
            self.apppend(value)
            return True
        before = self.get(index - 1)
        after = before.next
        new_node = Node(value)

        new_node.next = after
        before.next = new_node
        new_node.prev = before
        after.prev = new_node

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

        pre_node = self.get(index - 1)
        after_node = pre_node.next

        pre_node.next = after_node.next
        after_node.next = pre_node
        after_node = None
        self.length -= 1
        return True


dbl = DoublyLinkedList(1)
dbl.apppend(2)
dbl.apppend(3)
dbl.apppend(4)
dbl.apppend(5)
dbl.apppend(6)
dbl.apppend(7)
dbl.apppend(8)
dbl.apppend(9)
dbl.apppend(10)
# dbl.pop()
# dbl.prepend(76)
# dbl.pop_first()
# dbl.get(7)
# dbl.remove(4)
dbl.insert(5, 11)
dbl.printList()
