class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        temp_node = self.head
        result = ""

        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += " → "
            temp_node = temp_node.next
        return result

    """Inserting Element at the end of the SLL"""
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    """Inserting Element at the beginning of the SLL"""
    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    """Inserting Element at given index in SLL"""
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False

        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node

        elif index == 0:
            new_node.next = self.head
            self.head = new_node

        else:
            temp_node = self.head
            for _ in range(index - 1):          # Time Complexity: O(N)
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length += 1

    def traverse(self):
        current = self.head
        while current:                          # Time Complexity: O(N)
            print(current.value)
            current = current.next

    def search(self, target):
        index = 0
        current = self.head
        while current:                          # Time Complexity: O(N)
            if current.value == target:
                return index
            current = current.next
            index += 1
        return -1

    def get(self, index):
        if index == -1:
            return self.tail

        elif index < -1 or index >= self.length:
            return "Index out of bound"

        else:
            current = self.head
            for _ in range(index):              # Time Complexity: O(N)
                current = current.next
            return current

    def set_value(self, index, value):
        temp = self.get(index)                  # Time Complexity: O(N)
        if temp:
            temp.value = value
            return True
        return False

    def pop_first(self):
        if self.length == 0:
            return None
        popped_node = self.head
        if self.length == 1:            # this 'if' cond is because if SLL contain only one element in it.So delete tail
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            popped_node.next = None
        self.length -= 1
        return popped_node

    def pop(self):
        if self.length == 0:
            return False
        popped_node = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp = self.head
            while temp.next != self.tail:       # Time Complexity: O(N)
                temp = temp.next
            self.tail = temp
            temp.next = None
        self.length -= 1
        return popped_node

    def remove(self, index):
        if index < -1 or index >= self.length:
            return None
        elif index == 0:
            return self.pop_first()
        elif index == self.length - 1 or index == -1:
            return self.pop()                           # Time Complexity: O(N)
        else:
            prev_node = self.get(index-1)               # Time Complexity: O(N)
            popped_node = prev_node.next
            prev_node.next = popped_node.next
            popped_node.next = None
        self.length -= 1
        return popped_node

    def delete_all(self):
        self.head = None
        self.tail = None
        self.length = 0

new_linked_list = LinkedList()
new_linked_list.prepend(10)
new_linked_list.append(20)
new_linked_list.append(30)
new_linked_list.prepend(40)
print(new_linked_list)

print("Popped First Node:", new_linked_list.pop_first())
print(new_linked_list)

print("Popped Last Node: ", new_linked_list.pop())
print(new_linked_list)

new_linked_list.append(30)
print("tt  :", new_linked_list)

print(new_linked_list.remove(-1))
print(new_linked_list)

print(new_linked_list.tail.value)       # tail should contain last element not removed element

print(new_linked_list.delete_all())
