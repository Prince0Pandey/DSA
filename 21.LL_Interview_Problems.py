from Node_LinkedList_class import LinkedList
"""
    Remove Duplicates
Q1. Write a function to remove duplicates from an unsorted linked list.
Input 1 -> 2 -> 2 -> 3 -> 4 -> 4 -> 4 -> 5 
Output 1 -> 2 -> 3 -> 4 -> 5
"""


# def remove_duplicates(ll):
#     if ll.head is None:
#         return ll
#     else:
#         seen = set()
#         currNode = ll.head
#         prev_node = None
#         while currNode:
#             if currNode.value in seen:
#                 prev_node.next = currNode.next
#             else:
#                 seen.add(currNode.value)
#                 prev_node = currNode
#             currNode = currNode.next
#
#         return ll
#
# customLL = LinkedList()
# customLL.generate(10, 0, 99)
# print(customLL)
# print(remove_duplicates(customLL))

"""
    Return kth Element to the last
Q2. given linked list with n Element we have to return the kth element from the last node
"""


# def nthToLast(ll, n):
#     pointer1 = ll.head
#     pointer2 = ll.head
#     for _ in range(n):
#         if pointer2 is None:
#             return None
#         pointer2 = pointer2.next
#     while pointer2:
#         pointer1 = pointer1.next
#         pointer2 = pointer2.next
#     return pointer1
#
# customLL = LinkedList()
# customLL.generate(10, 0, 99)
# print(customLL)
# print(nthToLast(customLL, 5))

"""
    Partition
Q3. Write code to partiton a linked list around a value x, such that all node's value less than x come 
before all nodes greater than or equal to x
"""


# def partition(ll, x):
#     currNode = ll.head
#     ll.tail = ll.head
#
#     while currNode:
#         nextNode = currNode.next
#         currNode.next = None
#         if currNode.value < x:
#             currNode.next = ll.head
#             ll.head = currNode
#         else:
#             ll.tail.next = currNode
#             ll.tail = currNode
#         currNode = nextNode
#
#         if ll.tail.next is not None:
#             ll.tail.next = None
#
# customLL = LinkedList()
# customLL.generate(10, 0, 99)
# print(customLL)
# partition(customLL, 30)
# print(customLL)

"""
    Sum list
Q4. You have 2 numbers represented by a linked list, where each node contains a single digit.
The digits are stored in a reverse order, such that the first digit is at the head of the list.
Write a function that adds the two numbers and returns the sum as a linked list.

input:  list1 = 7 -> 1 -> 6      number1:617
        list2 = 5 -> 9 -> 2      number2:295
        sum: 617+295 = 912   
          
output: sumList = 2 -> 1 -> 9

Approach:   617     7+5   = 12
           +295     1+9+1 = 11
           -----    6+2+1 = 9
            912 
"""


# def sumList(lla, llb):
#     n1 = lla.head
#     n2 = llb.head
#     carry = 0
#     ll = LinkedList()
#
#     while n1 or n2:
#         result = carry
#         if n1:
#             result += n1.value
#             n1 = n1.next
#         if n2:
#             result += n2.value
#             n2 = n2.next
#         ll.add(int(result % 10))
#         carry = result/10
#     return ll
#
# lla = LinkedList()
# lla.add(7)
# lla.add(1)
# lla.add(6)
#
# llb = LinkedList()
# llb.add(5)
# llb.add(9)
# llb.add(2)
#
# print(lla)
# print(llb)
# print(sumList(lla, llb))

"""
    Intersection
Q5. Given two (singly) linked lists, determine if the two lists intersect.
Return the intersecting node.
Note that the intersection is defined based on reference, not value.
I.e if the kth node of the first linked list is the exact same node (by reference) as the 
jth node of the second linked list, then they are intersecting.

Example:
1. Non-Intersecting Linked List
    list1:    3 -> 1 -> 5 -> 9 -> 7 -> 2 -> 1
    list2:         2 -> 4 -> 6 -> 7 -> 2 -> 1

2. Intersecting Linked List
    list1:    3 -> 1 -> 5 -> 9 -> 7 -> 2 -> 1
    list2:         2 -> 4 -> 6 ↗
"""
# from Node_LinkedList_class import LinkedList, Node
#
#
# def intersection(lla, llb):
#     if lla.tail is not llb.tail:
#         return False
#
#     lenA = len(lla)
#     lenB = len(llb)
#
#     shorter = lla if lenA < lenB else llb
#     longer = llb if lenA < lenB else lla
#
#     diff = len(longer) - len(shorter)
#     longerNode = longer.head
#     shorterNode = shorter.head
#
#     for i in range(diff):
#         longerNode = longerNode.next
#
#     while shorterNode is not longerNode:
#         shorterNode = shorterNode.next
#         longerNode = longerNode.next
#
#     return longerNode
#
# # Helper addition method
# def addSameNode(lla, llb, value):
#     tempNode = Node(value)
#     lla.tail.next = tempNode
#     lla.tail = tempNode
#     llb.tail.next = tempNode
#     llb.tail = tempNode
#
# lla = LinkedList()
# lla.generate(3, 0, 10)
#
# llb = LinkedList()
# llb.generate(4, 0, 10)
#
# addSameNode(lla, llb, 12)
# addSameNode(lla, llb, 15)
#
# print(lla)
# print(llb)
#
# print(intersection(lla, llb))
# # Time Complexity: O(A+B)
