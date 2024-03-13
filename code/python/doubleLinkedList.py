class Node:
    def __init__(self) -> None:
        self.data = input("Enter data: ")
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def addLast(self):
        print("\nAdding last")
        newNode = Node()

        if self.head is None:
            self.head = newNode
            self.tail = newNode
            return
        
        newNode.prev = self.tail
        self.tail.next = newNode
        self.tail = newNode

    def addFirst(self):
        print("\nAdding first")
        newNode = Node()

        if self.head is None:
            self.head = newNode
            self.tail = newNode
            return
        
        newNode.next = self.head
        self.head.prev = newNode
        self.head = newNode

    def addMiddle(self):
        print("\nAdding middle")
        index = int(input("Add in index: "))
        if index == 0:
            self.addFirst()
            return

        temp = self.head

        for _ in range(index - 1):
            if temp.next is None:
                self.addLast()
                return
            
            temp = temp.next

        newNode = Node()
        newNode.prev = temp
        newNode.next = temp.next

        temp.next = newNode
        temp.next.prev = newNode
    
    def removeMiddle(self):
        print("\nRemoving middle")
        index = int(input("Remove in index: "))
        if index == 0:
            self.removeFirst()
            return

        temp = self.head

        for _ in range(index - 1):
            if temp.next is None:
                self.removeLast()
                return
            
            temp = temp.next

        temp.next = temp.next.next
        temp.next.prev = temp

    def removeByData(self):
        print("\nRemoving by data")
        data = input("Enter data to remove: ")
        temp = self.head

        while temp:
            if temp.data == data:
                if temp.prev is None:
                    self.removeFirst()
                    return
                if temp.next is None:
                    self.removeLast()
                    return
                temp.prev.next = temp.next
                temp.next.prev = temp.prev
                return
            temp = temp.next

    def removeFirst(self):
        self.head = self.head.next
        self.head.prev = None

    def removeLast(self):
        self.tail = self.tail.prev
        self.tail.next = None

    def printList(self):
        print("\nPrinting list")
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

dll = DoubleLinkedList()
dll.addLast()
dll.addLast()
dll.addMiddle()
dll.removeMiddle()
dll.addFirst()
dll.removeByData()
dll.printList()