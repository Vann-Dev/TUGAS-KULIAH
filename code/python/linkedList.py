class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def addFirst(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def addLast(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = newNode

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next

    def removeFirst(self):
        self.head = self.head.next

    def removeLast(self):
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None

ll = LinkedList()
ll.addLast(1)
ll.addLast(2)
ll.addFirst(2)
ll.removeFirst()
ll.removeLast()
ll.printList()
