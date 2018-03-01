class Stack:
    def __init__(self, *args):
        self.__items = []
        self.push(*args)

    def __str__(self):
        return str(self.peek())

    def __bool__(self):
        return not self.isEmpty()

    def __list__(self):
        return self.__items


    def __eq__(self, other):
        if isinstance(self, type(other)):
            return self.peek() == other.peek()
        else:
            return self.peek() == other

    def __ne__(self, other):
        if isinstance(self, type(other)):
            return self.peek() != other.peek()
        else:
            return self.peek() != other

    def __gt__(self, other):
        if isinstance(self, type(other)):
            return self.peek() > other.peek()
        else:
            return self.peek() > other

    def __lt__(self, other):
        if isinstance(self, type(other)):
            return self.peek() < other.peek()
        else:
            return self.peek() < other

    def __ge__(self, other):
        if isinstance(self, type(other)):
            return self.peek() >= other.peek()
        else:
            return self.peek() >= other

    def __le__(self, other):
        if isinstance(self, type(other)):
            return self.peek() <= other.peek()
        else:
            return self.peek() <= other

    def __iter__(self):
        for i in self.__items:
            yield i

    def isEmpty(self):
        return self.__items == []

    def push(self, *args):
        for item in args:
            self.__items.append(item)

    def pop(self):
        if self.isEmpty():
            return None
        else:
            return self.__items.pop()


    def peek(self):
        temp = self.pop()
        self.push(temp)
        return temp

    def __len__(self):
        return len(self.__items)
