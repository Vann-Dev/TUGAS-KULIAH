class Node:
    def __init__(self) -> None:
        self.data = None
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def addLast(self, data):
        newNode = Node()
        newNode.data = data

        if self.head is None:
            self.head = newNode
            self.tail = newNode
            return
        
        newNode.prev = self.tail
        self.tail.next = newNode
        self.tail = newNode

    def addFirst(self, data):
        newNode = Node()
        newNode.data = data

        if self.head is None:
            self.head = newNode
            self.tail = newNode
            return
        
        newNode.next = self.head
        self.head.prev = newNode
        self.head = newNode

    def addMiddle(self, data, index):
        if index == 0:
            self.addFirst(data)
            return

        temp = self.head

        for _ in range(index - 1):
            temp = temp.next

        newNode = Node()
        newNode.data = data
        newNode.prev = temp
        newNode.next = temp.next

        temp.next = newNode
        temp.next.prev = newNode

    def removeFirst(self):
        self.head = self.head.next
        self.head.prev = None

    def removeLast(self):
        self.tail = self.tail.prev
        self.tail.next = None

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next

dll = DoubleLinkedList()
dll.addLast(1)
dll.addLast(2)
dll.addLast(3)
dll.addMiddle(4, 1)
dll.addMiddle(100, 0)
dll.addMiddle(5, 2)
dll.addFirst(0)
dll.addMiddle(19, 7)
dll.printList()