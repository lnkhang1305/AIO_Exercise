class MyQueue():
    def __init__(self, capacity) -> None:
        self.frontier = []
        self.capacity = capacity

    def is_empty(self):
        return len(self.frontier) == 0

    def is_full(self):
        return len(self.frontier) == self.capacity

    def dequeue(self):
        return self.frontier.pop(0)

    def enqueue(self, value):
        self.frontier.append(value)

    def front(self):
        return self.frontier[0]


if __name__ == "__main__":
    queue1 = MyQueue(capacity=5)
    queue1.enqueue(1)
    queue1.enqueue(2)
    print(queue1.is_full())
    print(queue1.front())
    print(queue1.dequeue())
    print(queue1.front())
    print(queue1.dequeue())
    print(queue1.is_empty())
