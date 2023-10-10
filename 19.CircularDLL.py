class Node:
    def __init__(self, value=None):
        self.prev = None
        self.value = value
        self.next = None


class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break

    # Creation of circular doubly linked list
    def createCDLL(self, node_value):
        newNode = Node(node_value)
        self.head = self.tail = newNode.next = newNode.prev = newNode
        return "CDLL created successfully"

    # Insertion in the Linked List
    def insertNode(self, node_value, location):
        if self.head is None:
            return "Circular Doubly Linked List does not exist"

        else:
            newNode = Node(node_value)
            if location == 0:
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode    # we are providing prev reference to old head
                self.tail.next = newNode
                self.head = newNode

            elif location == -1:
                newNode.prev = self.tail
                newNode.next = self.head
                self.head.prev = newNode
                self.tail.next = newNode
                self.tail = newNode

            else:
                currNode = self.head
                index = 0
                while index < location - 1:
                    currNode = currNode.next
                    index += 1
                newNode.prev = currNode
                newNode.next = currNode.next
                newNode.next.prev = newNode
                currNode.next = newNode
            return "The node has been successfully inserted"

    # Traversal in Circular doubly linked list
    def travrseCDLL(self):
        if self.head is None:
            print("Circular doubly linked list is Empty")
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                if tempNode == self.tail:
                    break
                tempNode = tempNode.next

    # Reverse traversal in Circular doubly linked list
    def reverseTravrseCDLL(self):
        if self.head is None:
            print("Circular doubly linked list is Empty")
        else:
            tempNode = self.tail
            while tempNode:
                print(tempNode.value)
                if tempNode == self.head:
                    break
                tempNode = tempNode.prev

    # Search Node in Circular doubly linked list
    def searchCDLL(self, node_value):
        if self.head is None:
            return "Circular doubly linked list is Empty"
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == node_value:
                    return f"{node_value} present in Circular Linked List"
                if tempNode == self.tail:
                    break
                tempNode = tempNode.next
            return f"{node_value} does not present in Circular Linked List"

    # Delete a node from circular doubly linked list
    def deleteNode(self, location):
        if self.head is None:
            print("Circular linked list does not exist")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.next = self.head.prev = None
                    self.head = self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = self.tail
                    self.tail.next = self.head
            elif location == -1:
                if self.head == self.tail:
                    self.head.next = self.head.prev = None
                    self.head = self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.head.prev = self.tail
                    self.tail.next = self.head
            else:
                currNode = self.head
                index = 0
                while index < location - 1:
                    currNode = currNode.next
                    index += 1
                currNode.next = currNode.next.next
                currNode.next.prev = currNode
            print("The node has been successfully deleted")

    def deleteAll(self):
        if self.head is None:
            print("Circular doubly linked list does not exist")
        else:
            self.tail.next = None
            currNode = self.head
            while currNode:
                currNode.prev = None
                currNode = currNode.next
            self.head = None


circularDLL = CircularDoublyLinkedList()
circularDLL.createCDLL(20)
circularDLL.insertNode(10, 0)
circularDLL.insertNode(40, -1)
circularDLL.insertNode(30, 2)
print([node.value for node in circularDLL])

# circularDLL.travrseCDLL()
# circularDLL.reverseTravrseCDLL()
# print(circularDLL.searchCDLL(30))
# circularDLL.deleteNode(-1)
# circularDLL.deleteNode(3)
# circularDLL.deleteNode(0)
# print([node.value for node in circularDLL])
# circularDLL.deleteAll()
# print([node.value for node in circularDLL])
