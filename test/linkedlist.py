class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:
    def __init__(self):
        self.dummy = Node()

    def get(self, index):
        cur = self.dummy.next
        if cur == None:
            return -1
        for _ in range(index):
            if cur.next != None:
                cur = cur.next
        return cur.val

    def add_at_head(self, val):
        new_node = Node(val)
        new_node.next = self.dummy.next
        self.dummy.next = new_node

    def add_at_tail(self, val):
        cur = self.dummy
        while cur.next != None:
            cur =cur.next
        cur.next = Node(val)

    def add_at_index(self, val, index):
        new_node = Node(val)
        cur = self.dummy.next
        for _ in range(index):
            if cur.next != None:
                cur =cur.next
        new_node.next = cur.next
        cur.next = new_node

    def delete_at_index(self, index):
        cur = self.dummy.next
        for _ in range(index):
            if cur.next != None:
                cur =cur.next
        cur.next = cur.next.next