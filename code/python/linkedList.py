class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def addLast(self, data):
        newNode = Node(data)

        if self.head is None:
            self.head = newNode
            return

        temp = self.head

        while temp.next:
            temp = temp.next

        temp.next = newNode

    def addFirst(self, data):
        newNode = Node(data)

        if self.head is None:
            self.head = newNode
            return

        newNode.next = self.head
        self.head = newNode

    def addMiddle(self, data, index):
        if index == 0:
            self.addFirst(data)
            return

        temp = self.head

        for _ in range(index - 1):
            if temp.next is None:
                self.addLast(data)
                return

            temp = temp.next

        newNode = Node(data)
        newNode.next = temp.next
        temp.next = newNode

    def removeLast(self):
        if self.head is None:
            return

        if self.head.next is None:
            self.head = None
            return

        temp = self.head

        while temp.next.next:
            temp = temp.next

        temp.next = None

    def removeFirst(self):
        if self.head is None:
            return

        self.head = self.head.next

    def removeMiddle(self, index):
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

    def printList(self):
        temp = self.head

        while temp:
            print(temp.data)
            temp = temp.next

ll = LinkedList()
ll.addLast(1)
ll.addLast(2)
ll.addFirst(2)
ll.addMiddle(3, 1)
ll.printList()
ll.removeMiddle(1)
ll.printList()
ll.removeLast()
ll.printList()
