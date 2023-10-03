"""
    Reverse a Singly Linked List
Q1. Write a function to reverse a singly linked list. The function should return a new linked list that is the reverse of the original list.

Example:
Original singly linked list:   1 -> 2 -> 3 -> 4 -> 5
Reversed singly linked list:   5 -> 4 -> 3 -> 2 -> 1
"""


# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None
#
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.length = 0
#
#     def __str__(self):
#         temp_node = self.head
#         result = ''
#         while temp_node is not None:
#             result += str(temp_node.value)
#             if temp_node.next is not None:
#                 result += ' -> '
#             temp_node = temp_node.next
#         return result
#
#     def append(self, value):
#         new_node = Node(value)
#         if self.head is None:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.next = new_node
#             self.tail = new_node
#         self.length += 1
#
#     def reverse(self):
#         prev_node = None
#         current_node = self.head
#         while current_node is not None:
#             next_node = current_node.next
#             current_node.next = prev_node
#             prev_node = current_node
#             current_node = next_node
#         self.head, self.tail = self.tail, self.head
#
# new_list = LinkedList()
# new_list.append(10)
# new_list.append(20)
# new_list.append(30)
# new_list.append(40)
# new_list.append(50)
# print(new_list)
# new_list.reverse()
# print(new_list)

"""
    Remove Duplicates from a Singly Linked List
Q2. Given a singly linked list, write a function that removes all the duplicates. use this linked list .

Example:
Original Linked List - "1 -> 2 -> 4 -> 3 -> 4 -> 2"
Result Linked List   - "1 -> 2 -> 4 -> 3
"""


# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None
#
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.length = 0
#
#     def __str__(self):
#         temp_node = self.head
#         result = ''
#         while temp_node is not None:
#             result += str(temp_node.value)
#             if temp_node.next is not None:
#                 result += ' -> '
#             temp_node = temp_node.next
#         return result
#
#     def append(self, value):
#         new_node = Node(value)
#         if self.head is None:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.next = new_node
#             self.tail = new_node
#         self.length += 1
#
#     def remove_duplicates(self):
#         if self.head is None:
#             return
#         node_values = set()  # set to store unique node values
#         current_node = self.head
#         node_values.add(current_node.value)
#         while current_node.next:
#             if current_node.next.value in node_values:  # duplicate found
#                 current_node.next = current_node.next.next
#                 self.length -= 1
#             else:
#                 node_values.add(current_node.next.value)
#                 current_node = current_node.next
#         self.tail = current_node
#
# new_list = LinkedList()
# new_list.append(10)
# new_list.append(20)
# new_list.append(10)
# new_list.append(40)
# new_list.append(20)
# new_list.append(30)
# new_list.append(50)
# new_list.append(40)
# print(new_list)
# new_list.remove_duplicates()
# print(new_list)

"""
    Merge Two Sorted Linked List
Q3. You are given the heads of two sorted linked lists list1 and list2. Merge the two lists in a one sorted list.
The list should be made by splicing together the nodes of the first two lists. Return the head of the merged 
linked list.   

Example 1: 
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3: 
Input: list1 = [], list2 = [0]
Output: [0]

Constraints: 
The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):

    def mergeTwoLists(self, l1, l2):
        prehead = ListNode(-1)
        prev = prehead

        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next

        # At least one of l1 and l2 can still have nodes at this point, so connect the non-null
        # list to the end of the merged list.
        prev.next = l1 if l1 is not None else l2

        return prehead.next
