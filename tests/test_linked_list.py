import random
from unittest import TestCase

from common.linked_list import Node, LinkedList, NodeData


class TestLinkedList(TestCase):
    """
    Test runner for the LinkedList class to ensure expected behavior from the
    methods and properties across varying operations.
    """
    @staticmethod
    def _create_node(data: NodeData) -> Node:
        """
        Helper method to create a Node object
        Args:
            data: value that is encapsulated by the Node object's <val> property.

        Returns:
            Node object with <val> set as val property.
        """
        return Node(data=data)

    def test_create_node(self):
        """
        Tests that Node class objects are created as expected
        """
        num1 = 1
        node1 = self._create_node(data=num1)
        self.assertTrue(node1.data == num1)

        num2 = 2
        node2 = self._create_node(num2)
        node1.next = node2
        self.assertTrue(node1.next.data == node2.data)

    def test_create_linked_list(self):
        """
        Tests that a LinkedList object can be created.
        """
        ll = LinkedList()

        # test ll object is created and initial properties are expected values.
        self.assertTrue(ll is not None)
        self.assertTrue(type(ll) == LinkedList)
        self.assertTrue(ll.head == ll.tail is None)
        self.assertTrue(ll.length == 0)

    def test_length_property(self):
        """
        Tests that the length property functions as expected with an
        <insert> or <pop> command is given.
        """
        vals = [0, 1, 2]
        ll = LinkedList()

        # assert length initialized to 0
        self.assertTrue(ll.length == 0)

        # test <length> property increments as expected
        for i, item in enumerate(vals):
            ll.insert(data=item)
            self.assertTrue(ll.length == i+1)

        # test <length> property decrements as expected
        for i, item in enumerate(vals):
            node = ll.pop()
            self.assertTrue(type(node) == Node)
            self.assertTrue(ll.length == len(vals) - (i+1))

    def test_insert(self):
        """
        Tests adding a value into the linked list.
        """
        ll = LinkedList()
        val1 = 3
        val2 = 6
        val3 = 9

        # execute first insert, verify state
        ll.insert(data=val1)
        self.assertTrue(ll.head.data == val1)
        self.assertTrue(ll.tail.data == val1)
        self.assertTrue(ll.head.next == ll.tail)

        # execute second insert, verify state
        ll.insert(data=val2)
        self.assertTrue(ll.head.data == val1)
        self.assertTrue(ll.tail.data == val2)
        self.assertTrue(ll.head != ll.tail)
        self.assertTrue(ll.head.next == ll.tail)

        # execute third insert, verify state
        ll.insert(data=val3)
        self.assertTrue(ll.head.data == val1)
        self.assertTrue(ll.tail.data == val3)
        self.assertTrue(ll.head.next != ll.tail)

    def test_insert_all(self):
        """
        Tests the <insert_all> method via which multiple items can be added
        to a LinkedList object.
        Note: uses the <insert> method that is already tested at this point.
        """
        # vals are always 50 random digits 1-10 inclusive
        vals = [random.choice(range(1, 11)) for _ in range(50)]

        # create the list, add the data
        ll = LinkedList()
        ll.insert_all(data=vals)

        # confirm references are to values as expected
        next = ll.head
        i = 0
        while next is not None:
            self.assertTrue(next.data == vals[i])
            next = next.next
            i += 1
        self.assertTrue(ll.tail.data == vals[-1])

    def test_str(self):
        """
        Tests that the __str__ method produces the expected output.
        """
        vals = [0, 1, 2, 3]
        ll = LinkedList()
        ll.insert_all(data=vals)

        self.assertTrue(ll.__str__() == "|0| -> |1| -> |2| -> |3|")
