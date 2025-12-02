# pylint: disable=too-few-public-methods
"""A class for a doubly-linked, circular linked list"""

from collections.abc import Iterable


class Node:
    """A single Node"""

    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


class CircularLinkedList:
    """A CircularLinkedList class"""

    def __init__(self):
        self.head = None

    def __len__(self):
        cur = self.head
        count = 0
        while cur:
            count += 1
            cur = cur.next
            if cur == self.head:
                break
        return count

    def __iter__(self):
        cur = self.head
        while cur:
            yield cur.data
            cur = cur.next
            if cur == self.head:
                break

    def __repr__(self):
        return str(list(self))

    def append(self, data):
        """Append a new element"""
        if self.head is None:
            self.head = Node(data)
            self.head.next = self.head
            self.head.prev = self.head
        else:
            new_node = Node(data)
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.prev = current
            new_node.next = self.head
            self.head.prev = new_node

    @classmethod
    def from_iterable(cls, obj):
        """Create a new CircularLinkedList from an iterable"""
        if not isinstance(obj, Iterable):
            raise TypeError("Object does not support iteration")
        new_list = cls()
        for elem in list(obj):
            new_list.append(elem)
        return new_list
