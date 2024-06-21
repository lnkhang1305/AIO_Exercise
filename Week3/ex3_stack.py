class Node():
    def __init__(self, value=0, next=None) -> None:
        self.value = value
        self.next = next

class MyStack():
    def __init__(self, capacity) -> None:
        self.head = None
        self.tail = None
        self.capacity = capacity
    def is_empty(self):
        return self.head == None
    def __len__(self):
        if self.is_empty():
            return 0 
        count = 1
        cur = self.head
        while cur.next is not None:
            count += 1
            cur = cur.next
        return count
    def is_full(self):
        return len(self) == self.capacity
    def pop(self):
        if self.is_empty():
            print('Stack is empty')
            return None
        if len(self) == 1:
            value = self.head.value
            self.head = None
            self.tail = None
            return value
        cur = self.head
        while cur.next != self.tail:
            cur = cur.next
        value = self.tail.value
        cur.next = None
        self.tail = cur
        return value
    def push(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            return None
        if self.is_full():
            print('Stack is full')
            return None
        if len(self) == 1:
            self.head.next = new_node
            self.tail = new_node
            return None
        self.tail.next = new_node
        self.tail = new_node
    def top(self):
        return self.tail.value
    def print(self):
        if self.is_empty():
            print('Stack is empty')
            return ''
        cur = self.head
        while cur is not None:
            print(cur.value, end=' ')
            cur = cur.next
    
if __name__ == "__main__":
    stack1 = MyStack(capacity=5)
    stack1.push(1)
    stack1.push(2)
    stack1.push(3)
    print(stack1.top())
    print(stack1.pop())
    print(stack1.pop())
    print(stack1.pop())
    print(stack1.is_empty())