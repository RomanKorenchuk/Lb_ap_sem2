class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
        self.prev = None
        self.next = None

class PriorityQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, value, priority): 
        new_node = Node(value, priority)
        if self.head is None:
            self.head = self.tail = new_node
            return
        current = self.head
        while current and current.priority >= priority:
            current = current.next
        if current is None:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        elif current == self.head:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        else:
            prev_node = current.prev
            prev_node.next = new_node
            new_node.prev = prev_node
            new_node.next = current
            current.prev = new_node

    def pop(self):
        if self.head is None:
            return None
        value = self.head.value
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        return value

    def peek(self):
        if self.head is None:
            return None
        return self.head.value

    def __str__(self):
        result = []
        current = self.head
        while current:
            result.append(str(current))
            current = current.next
        return " <-> ".join(result)
