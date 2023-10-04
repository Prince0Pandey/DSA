"""
    Reverse a Singly Linked List
Q1. Write a function to reverse a singly linked list. The function should return a new linked list
that is the reverse of the original list.

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
Q2. Given a singly linked list, write a function that removes all the duplicates. use this linked list.

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
Q3. You are given the heads of two sorted linked lists list1 and list2. Merge the two lists in a one 
sorted list. The list should be made by splicing together the nodes of the first two lists. Return the
head of the merged linked list.   

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


# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
#
# class Solution:
#
#     def mergeTwoLists(self, l1, l2):
#         prehead = ListNode(-1)
#         prev = prehead
#
#         while l1 and l2:
#             if l1.val <= l2.val:
#                 prev.next = l1
#                 l1 = l1.next
#             else:
#                 prev.next = l2
#                 l2 = l2.next
#             prev = prev.next
#
#         # At least one of l1 and l2 can still have nodes at this point, so connect the non-null
#         # list to the end of the merged list.
#         prev.next = l1 if l1 is not None else l2
#         return prehead.next

"""
    Remove Duplicates
Q4. Given the head of a sorted linked list, delete all duplicates such that each element appears only
once. Return the linked list sorted as well. 

Example 1:
Input: head = [1,1,2]
Output: [1,2]

Example 2:
Input: head = [1,1,2,3,3]
Output: [1,2,3]
"""


# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
#
# class Solution:
#     def deleteDuplicates(self, head):
#         current_node = head
#
#         while current_node is not None and current_node.next is not None:
#             if current_node.val == current_node.next.val:
#                 current_node.next = current_node.next.next
#             else:
#                 current_node = current_node.next
#
#         return head

"""
    Remove Linked List Elements
Q5. Given the head of a linked list and an integer val, remove all the nodes of the linked list 
    that has Node.val == val, and return the new head.

Example 1:
Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]

Example 2:
Input: head = [], val = 1
Output: []

Example 3:
Input: head = [7,7,7,7], val = 7
Output: []

Constraints:
The number of nodes in the list is in the range [0, 104].
1 <= Node.val <= 50
0 <= val <= 50
"""


# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
#
# class Solution:
#     def removeElements(self, head, val):
#         dummy_head = ListNode(-1)
#         dummy_head.next = head
#
#         prev_node, curr_node = dummy_head, head
#         while curr_node:
#             if curr_node.val == val:
#                 prev_node.next = curr_node.next
#             else:
#                 prev_node = curr_node
#             curr_node = curr_node.next
#
#         return dummy_head.next

"""
    Reverse Linked List
Q6. Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []

Constraints:
The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
"""


# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
#
# class Solution:
#     def reverseList(self, head):
#         prev_node = None
#         curr_node = head
#
#         while curr_node is not None:
#             next_node = curr_node.next
#             curr_node.next = prev_node
#             prev_node = curr_node
#             curr_node = next_node
#         return prev_node

"""
    Palindrome Linked List(did not understand)
Q7. Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

Example 1:
Input: head = [1,2,2,1]
Output: true

Example 2:
Input: head = [1,2]
Output: false

Constraints:
The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9
"""


# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
#
# class Solution:
#     def isPalindrome(self, head):
#         slow = fast = head
#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next
#
#         prev = None
#         while slow:
#             nxt = slow.next
#             slow.next = prev
#             prev = slow
#             slow = nxt
#
#         while prev:
#             if head.val != prev.val:
#                 return False
#             head = head.next
#             prev = prev.next
#         return True

"""
    Middle of the Linked List
Q8. Given the head of a singly linked list, return the middle node of the linked list. If there are two
middle nodes, return the second middle node.

Example 1:
Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

Example 2:
Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.

Constraints:
The number of nodes in the list is in the range [1, 100].
1 <= Node.val <= 100
"""

"""MY WAY"""
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
#
# def length(head):
#     count = 0
#     while head:
#         count += 1
#         head = head.next
#     return count
#
#
# class Solution:
#     def middleNode(self, head):
#         total_node = length(head)
#         for _ in range(int(total_node / 2)):
#             head = head.next
#         return head

"""2nd WAY"""
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
#
# class Solution(object):
#     def middleNode(self, head):
#         fast = head
#         while fast and fast.next:
#             head = head.next
#             fast = fast.next.next
#
#         return head
