"""
Given an array of integers nums and an integer target, return indices of the two
numbers such that they add up to target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

You can return the answer in any order.
"""
from typing import List
from unittest import TestCase


def two_sum(nums: List[int], target: int) -> List[int]:
    """
    Checks the array nums for two elements that add to the value <target> and
    returns their indices in any order.
    Args:
        nums: a collection of integer values
        target: the value to be summed to.

    Returns:
        Indices
    """
    hashed = {}
    for i, num in enumerate(nums):

        # if the compliment of the number and target exists, return
        # the value of current number and compliment index as solution.
        if target - num in hashed:
            return [i, hashed[target - num]]

        # if the complement does not exist, add the current number to
        # the hashmap such that its index within <nums> is the value.
        hashed[num] = i

    raise Exception("two_sum shouldn't reach this far as all <nums> arguments"
                    " should contain a valid solution.")


class TestTwoSum(TestCase):
    """
    Tests the two_sum function against various test conditions
    """
    def setUp(self) -> None:
        self.function = two_sum

    def _good(self, a: List[int], b: List[int]):
        """Checks that all items in a are in b, in no particular order"""
        return all(x in b for x in a)

    def test_case_1(self):
        self.assertTrue(self._good(self.function([2, 7, 11, 15], 9), [0, 1]))
