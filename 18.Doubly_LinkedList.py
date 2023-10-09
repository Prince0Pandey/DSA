class Node:
    def __init__(self, value):
        self.prev = None
        self.value = value
        self.next = None


# noinspection PyMethodMayBeStatic
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    # Creation of Doubly Linked List
    def createDLL(self, nodevalue):
        node = Node(nodevalue)
        node.prev = None
        node.next = None
        self.head = node
        self.tail = node
        return "DLL is created successfully"

    # Insertion Method in Doubly Linked List
    def insertNode(self, nodevalue, location):
        if self.head is None:
            print("Node cannot be inserted")
        else:
            newNode = Node(nodevalue)
            if location == 0:
                newNode.prev = None
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode
            elif location == -1:
                newNode.next = None
                newNode.prev = self.tail
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                newNode.prev = tempNode
                newNode.next = tempNode.next
                tempNode.next = newNode
                newNode.next.prev = newNode

    # Traversal method in DLL
    def traverseDLL(self):
        if self.head is None:
            print("There is no Element to traverse")
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next

    # Reverse traversal in DLL
    def reverseTraversal(self):
        if self.head is None:
            print("There is no Element to traverse")
        else:
            tempNode = self.tail
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.prev

    # Search method in DLL
    def searchDLL(self, value):
        if self.head is None:
            return "No element in the List"
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == value:
                    return True
                tempNode = tempNode.next
            return False

    # Delete Node from DLL
    def deleteNode(self, location):
        if self.head is None:
            print("No element in the list")

        elif location == 0:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None

        elif location == -1:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.tail = self.tail.prev
                self.tail.next = None

        else:
            tempNode = self.head
            index = 0
            while index < location - 1:
                tempNode = tempNode.next
                index += 1
            tempNode.next = tempNode.next.next
            tempNode.prev = tempNode
        print("The Node is successfully Deleted")

    # Delete entire DLL
    def deleteDLL(self):
        if self.head is None:
            print("DLL is empty")
        else:
            currNode = self.head.next
            while currNode:
                currNode.prev = None
                currNode = currNode.next
            self.head = None
            self.tail = None
        print("DLL successfully Deleted")

doublyLL = DoublyLinkedList()
doublyLL.createDLL(30)

doublyLL.insertNode(10, 0)
doublyLL.insertNode(40, -1)
doublyLL.insertNode(50, -1)
doublyLL.insertNode(60, -1)
doublyLL.insertNode(70, -1)

print([node.value for node in doublyLL])
# doublyLL.traverseDLL()
# doublyLL.reverseTraversal()
# print(doublyLL.searchDLL(3))

# doublyLL.deleteNode(-1)
# print([node.value for node in doublyLL])
#
# doublyLL.deleteNode(2)
# print([node.value for node in doublyLL])
#
# doublyLL.deleteNode(0)
# print([node.value for node in doublyLL])

doublyLL.deleteDLL()
print([node.value for node in doublyLL])
