class Node:
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "<Node Data: %s>" % self.data        #'%s' means string and after that % for value that we want
        #return f"Node Data : {self.data}"

n1 = Node(10)
n1.next_node = 25
print(n1)
print("<Next_Node: ",n1.next_node,">", sep="")