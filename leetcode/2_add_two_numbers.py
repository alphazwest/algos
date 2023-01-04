"""
Problem:

You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a
single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the
number 0 itself.

Constraints:

1. The number of nodes in each linked list is in the range [1, 100].
2. 0 <= Node.val <= 9
3. It is guaranteed that the list represents a number that does not have leading
zeros.

From here:
    https://leetcode.com/problems/add-two-numbers/
"""
from common.linked_list import LinkedList, Node









def first_try(l1, l2):
    ...




def add_two_numbers(l1: List[int], l2: List[int]) -> List[int]:
    """
    Interprets the two lists as integer values, in reverse order, and
    adds them using simple addition.

    Examples:
        l1: [1, 2, 3]
        l2: [4, 3, 5]
        result: 321 + 531 = 852 == [2, 5, 8]

    Returns:
        list of integers representing a number in reverse order
    """
    return first_try(l1, l2)


if __name__ == "__main__":

    # define test cases
    a1 = [2, 4, 3]
    a2 = [5, 6, 4]
    b1 = [0]
    b2 = [0]
    c1 = [9, 9, 9, 9, 9, 9, 9]
    c2 = [9, 9, 9, 9]


    l = Node.from_list(a1)
    print(l)

