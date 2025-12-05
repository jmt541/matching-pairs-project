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
    

    def remove(self, value):
        temp  = self.head
        prev = None

        while temp is not None:
            if temp.value == value:
                if prev is None:
                    self.head = temp.next
            

                else:
                    prev.next = temp.next

                return
            
            prev = temp
            temp = temp.next


    def getSize(self):
        size  = 0
        temp  = self.head
        while temp is not None and temp.next is not None:
            size+=1
            temp = temp.next

        return size
    

    def getValueAtIndex(self, index):
        temp = self.head
        indexTemp  = 0
        while temp is not None:
            if index == indexTemp:
                return temp.value
            
            
            indexTemp +=1
            temp = temp.next


        





        


        

