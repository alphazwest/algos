from typing import Iterable, TypeVar, NoReturn

# define a generic type for NodeData to encapsulate
NodeData = TypeVar("NodeData")


class Node:
    """
    Structure to encapsulate data and maintain reference to the next item
    in a LinkedList class object.
    """
    def __init__(self, data: NodeData, next: "Node" = None):
        self.data = data
        self.next = next


class LinkedList:
    """
    Implementation of the LinkedList data structure with pointers to both the
    first (head) and last (tail) Node objects and reference to the total number
    of items referenced (length)
    """
    def __init__(self):
        self.head: Node = None
        self.tail: Node = None
        self.length: int = 0

    def insert(self, data: NodeData) -> NoReturn:
        """
        Add data as a Node object at the end of the LinkedList in O(1) time.
        Args:
            data: data to be encapsulated in a node
        """
        node = Node(data=data)

        if self.length == 0:
            self.head = self.tail = node
            self.head.next = self.tail

        else:
            # update last node reference to new insert
            prev_tail = self.tail
            self.tail = node
            prev_tail.next = node

        self.length += 1

    def insert_all(self, data: Iterable[NodeData]) -> NoReturn:
        """
        Given an iterable of NodeData, perform inserts for all items such that
        the LinkedList state will result in the <tail> property referencing the
        last element in <data>
        Args:
            data: an iterable of data to be inserted, item-wise, into the LL.
        """
        for d in data:
            self.insert(data=d)

    def pop(self) -> Node:
        """
        Removes and returns the last Node element in the Linked List in O(n).
        Returns:
            The Node object having been removed (previous tail) or None if
            there are no items currently in the LL.
        """
        if not self.head:
            return None

        if self.length == 1:
            popped = self.head
            self.head = self.tail = None
            self.length -= 1
            return popped

        # traverse the entire LL and get reference to the second
        # to last element, making it the new tail, and removing
        # the existing tail.
        popped = self.tail
        next = self.head
        while next is not None:
            prev = next         # second to last
            next = next.next    # tail

        self.tail = prev
        self.tail.next = None
        self.length -= 1
        return popped

    def __str__(self) -> str:
        """
        A LinkedList, encapsulating the data [0, 1, 2, 3], is represented as:
            |0| -> |1| -> |2| -> |3|

        Returns:
            string in the format of |0| -> |1| --> ... |n| where n is the total
            number of elements having been added.
        """
        output = ""
        next = self.head
        while next is not None:
            if next is not self.tail:
                output += f"|{next.data}| -> "
            else:
                output += f"|{next.data}|"
            next = next.next

        return output
