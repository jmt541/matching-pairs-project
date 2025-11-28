class Node:
    def __init__ (self, value, kartuDepanPath = None):
        self.value = value
        self.kartuDepanPath = kartuDepanPath
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


    def append(self, value, kartuDepanPath = None):
        new_node = Node(value, kartuDepanPath)


        if self.head is None:
            self.head = new_node
            return
        
        temp = self.head

        while temp.next:
            temp = temp.next
        temp.next = new_node


    # di convert ke py list untuk shuffling setelah di masukkan ke LL
    def convertList(self):
        arr = []
        temp = self.head

        while temp:
            arr.append((temp.value, temp.kartuDepanPath))
            temp = temp.next

        return arr
