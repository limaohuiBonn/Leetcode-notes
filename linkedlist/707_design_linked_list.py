class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class MyLinkedList:
    def __init__(self):
        self._dummy = Node(0)
        self._size = 0

    # def get(self, index: int) -> int:
    #     cur = self._dummy
    #     if index<0 or index>self._size-1:
    #         return
    #     while index:
    #         cur = cur.next
    #         index -= 1
    #     return cur.next.val

    def get(self, index: int) -> int:
        if index < 0 or index >= self._size:
            return -1

        cur = self._dummy
        for _ in range(index):
            cur = cur.next

        return cur.next.val

    def addAtHead(self, val: int) -> None:
        cur = self._dummy
        new_Node = Node(val)
        new_Node.next = cur.next
        self._dummy.next = new_Node
        self._size += 1

    def addAtTail(self, val: int) -> None:
        cur = self._dummy
        new_Node = Node(val)
        while cur.next:
            cur = cur.next
        cur.next = new_Node
        self._size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        cur = self._dummy
        new_Node = Node(val)
        if index < 0 or index > self._size:
            return
        while index:
            cur = cur.next
            index -= 1
        new_Node.next = cur.next
        cur.next = new_Node
        self._size += 1

    def deleteAtIndex(self, index: int) -> None:
        cur = self._dummy
        if index < 0 or index > self._size - 1:
            return
        while index:
            cur = cur.next
            index -= 1
        cur.next = cur.next.next
        self._size -= 1
