class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_stack(self):
        temp = self.top
        while(temp is not None):
            print(temp.value)
            temp = temp.next
        return True

    def push_stack(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node

        self.height += 1
        return True

    def push_pop(self):
        if self.height == 0:
            return None

        if self.height == 1:
            self.top = None
            return True
        temp = self.top
        self.top = self.top.next
        temp.value = None
        temp.next = None
        self.height -= 1
        return True


obj = Stack(1)
obj.push_stack(7)
obj.push_stack(8)
obj.push_pop()
obj.print_stack()
