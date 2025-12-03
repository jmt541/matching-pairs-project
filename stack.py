class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)


    def pop(self):
        if self.items:
            return self.items.pop()
        return None
    

    def size(self):
        return len(self.items)


    def is_empty(self):
        if (len(self.items) == 0):
            return True
        else:
            return False
        

    def clear(self):
        self.items = []
