import random

class Node:
    def __init__(self, value, kartuDepanPath=None):
        self.value = value
        self.kartuDepanPath = kartuDepanPath
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value, kartuDepanPath=None):
        new_node = Node(value, kartuDepanPath)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def getSize(self):
        size = 0
        temp = self.head
        while temp:
            size += 1
            temp = temp.next
        return size

    def getNodeAtIndex(self, index):
        temp = self.head
        indexTemp = 0
        while temp:
            if indexTemp == index:
                return temp
            indexTemp += 1
            temp = temp.next
        return None

    def shuffle(self):
        size = self.getSize()
        for i in range(size - 1, 0, -1):
            j = random.randint(0, i)

            node_i = self.getNodeAtIndex(i)
            node_j = self.getNodeAtIndex(j)

            # swap data
            node_i.value, node_j.value = node_j.value, node_i.value
            node_i.kartuDepanPath, node_j.kartuDepanPath = node_j.kartuDepanPath, node_i.kartuDepanPath

    # optional: convert to python list for debugging
    def convertList(self):
        arr = []
        temp = self.head
        while temp:
            arr.append((temp.value, temp.kartuDepanPath))
            temp = temp.next
        return arr
