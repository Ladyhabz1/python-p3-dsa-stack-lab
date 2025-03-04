class Stack:
    def __init__(self, limit=None):
        self.stack = []
        self.limit = limit  # Optional limit for stack size

    def push(self, value):
        if self.limit is not None and len(self.stack) >= self.limit:
            raise OverflowError("Stack is full")
        self.stack.append(value)

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from an empty stack")
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return len(self.stack) == 0

    def is_full(self):
        if self.limit is None:
            return False
        return len(self.stack) >= self.limit

    def search(self, value):
        try:
            return len(self.stack) - 1 - self.stack[::-1].index(value)
        except ValueError:
            return -1

# Example usage
if __name__ == "__main__":
    s = Stack(limit=5)
    s.push(10)
    s.push(20)
    s.push(30)
    print(s.search(20))  # Output: 1
    print(s.pop())       # Output: 30
    print(s.size())      # Output: 2
    print(s.is_empty())  # Output: False
    print(s.is_full())   # Output: False
