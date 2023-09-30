print()
"""
-> Linked List:

1. Linked List is a form of a sequential collection, and it does not have to be in order.
A Linked list is made up of independent nodes that may contain any type of data and each node has a reference
to the next node in the link.

2. Each node contains 2 part i.e Data & Link(Reference of physical location in memory) to next Node
NOTE: Linked List Nodes are not contiguously stored in memory.

3. Linked List have Head and Tail. Head store's address of first node & Tail store's address of Last node

4. Last node contains Data and NULL


-> TYPES OF LINKED LIST

1. Singly Linked List: Node stores only forward node's memory address & last node store Null in place of address

2. Circular Singly Linked List: Same as SLL but Last node store's Reference to first Node

3. Doubly Linked List: Contains reference of Previous & forward node 
NOTE: First Node contains Null as there is no previous node & Last node Contains Null as there is no forward node.
       
4. Circular Doubly Linked List: Same as DLL but First node store's the reference to last node & Last node store's
reference to first node
"""


# Empty Linked List
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0


new_linked_list1 = LinkedList()
print("Empty Linked List's Head Address:", new_linked_list1.head)
print("Empty Linked List's Tail Address:", new_linked_list1.tail)
print("Empty Linked List's Length:", new_linked_list1.length, "\n")


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


# Linked List with 1 Node
class LinkedList1:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

new_linked_list2 = LinkedList1(10)
print("Linked List with Single Element(Head Address):", new_linked_list2.head)
print("Linked List with Single Element(Tail Address):", new_linked_list2.tail)
print("Linked List with Single Element(Value using Head):", new_linked_list2.head.value)
print("Linked List with Single Element(Value using Tail)", new_linked_list2.tail.value)
print("Linked List with Single Element(Length):", new_linked_list2.length)

