class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

"""CSLL with 1 Element"""
# class CSLinkedList:
#     def __init__(self, value):
#         new_node = Node(value)
#         new_node.next = new_node
#         self.head = new_node
#         self.tail = new_node
#         self.length = 1
#
# cslinkedlist = CSLinkedList(10)
# print(cslinkedlist.head.value)

"""CSLL with No Element"""
class CSLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        temp_node = self.head
        result = ""
        while temp_node is not None:
            result += str(temp_node.value)
            temp_node = temp_node.next
            if temp_node == self.head:
                break
            result += " → "
        return result

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = new_node
        self.length += 1

    def insert_element(self, index, value):
        new_node = Node(value)
        if index < 0 or index > self.length:
            raise Exception("Index out of range")

        if index == 0:
            if self.length == 0:
                self.head = new_node
                self.tail = new_node
                new_node.next = new_node
            else:
                new_node.next = self.head
                self.head = new_node
                self.tail.next = new_node

        elif index == self.length:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node

        else:
            temp_node = self.head
            for _ in range(index-1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length += 1

    def traverse(self):
        # current = self.head
        # for _ in range(self.length-1):
        #     print(current.value, end=" ")
        #     current = current.next

        current = self.head
        while current is not None:
            print(current.value)
            current = current.next
            if current == self.head:
                break

    def search(self, element):
        current = self.head
        while current is not None:
            if current.value == element:
                return True
            current = current.next
            if current == self.head:
                break
        return False

    def get(self, index):
        if index == -1:
            return self.tail
        elif index < -1 or index >= self.length:
            raise Exception("Index out of range")

        current_node = self.head
        for _ in range(index):
            current_node = current_node.next
        return current_node

    def set_value(self, index, value):
        current_node = self.get(index)          # Time Complexity:O(N)
        if current_node:
            current_node.value = value
            return True
        return False

        # if index < -1 or index >= self.length:
        #     raise Exception("Index out of range")
        # elif index == -1:
        #     self.tail.value = value
        # else:
        #     current_node = self.head
        #     for _ in range(index):
        #         current_node = current_node.next
        #     current_node.value = value

    def pop_first(self):
        popped_node = self.head
        if self.head == 0:
            return None
        elif self.length == 1 :
            self.head = None
            self.tail = None
            return popped_node
        else:
            self.head = self.head.next
            self.tail.next = self.head
            popped_node.next = None
            self.length -= 1
            return popped_node

    def pop(self):
        popped_node = self.tail
        current_node = self.head

        if self.head is None:
            return None
        elif self.length == 1:
            self.head = self.tail = None
        else:
            while current_node.next != self.tail:       # Time Complexity: O(N)
                current_node = current_node.next
            current_node.next = self.head
            self.tail = current_node
            popped_node.next = None
        self.length -= 1
        return popped_node

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        elif index == 0:
            return self.pop_first()
        elif index == self.length-1:
            return self.pop()                   # Time Complexity: O(N)

        prev_node = self.get(index-1)           # Time Complexity: O(N)
        popped_node = prev_node.next
        prev_node.next = popped_node.next
        popped_node.next = None
        self.length -= 1
        return popped_node

        # prev_node = self.head
        # for _ in range(index-1):
        #     prev_node = prev_node.next
        # popped_node = prev_node.next
        # prev_node.next = popped_node.next
        # popped_node.next = None
        # self.length -= 1
        # return popped_node

    def delete_all(self):
        if self.length == 0:
            return
        self.tail.next = None
        self.head = None
        self.tail = None
        self.length = 0


cslinkedlist = CSLinkedList()
cslinkedlist.append(30)
cslinkedlist.append(40)
print(cslinkedlist)

cslinkedlist.prepend(20)
cslinkedlist.prepend(10)
print(cslinkedlist)

cslinkedlist.insert_element(4, 50)
print(cslinkedlist)

cslinkedlist.append(60)
print(cslinkedlist)

# cslinkedlist.insert_element(0, 90)
# print(cslinkedlist)
#
# cslinkedlist.traverse()
#
# print(cslinkedlist.search(900))
#
# print(cslinkedlist.get(4))
#
# cslinkedlist.set_value(-1, 80)
# print(cslinkedlist)
#
# print(cslinkedlist.pop_first())
# print(cslinkedlist)
#
# print(cslinkedlist.pop())
# print(cslinkedlist)
#
# print(cslinkedlist.remove())
# print(cslinkedlist)
#
# print(cslinkedlist.delete_all())
# print(cslinkedlist)
