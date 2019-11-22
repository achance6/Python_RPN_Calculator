class Stack:
    """Implementation of a stack using lists. Apparently a list is pretty ok but whatever."""

    def __init__(self):
        # Shouldn't declare as class var!
        self._stack = []

    def empty(self):
        return len(self._stack) == 0

    def size(self):
        return len(self._stack)

    def peek(self):
        return self._stack[len(self._stack) - 1]

    def push(self, val):
        self._stack.append(val)

    def pop(self):
        val = self._stack[len(self._stack) - 1]
        del self._stack[len(self._stack) - 1]
        return val

    def __contains__(self, val):
        return self._stack.__contains__(val)
