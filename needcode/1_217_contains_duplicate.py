"""
Number 1 in the arrays problem from NeetCode.io in reference to the problem 217
in LeetCode.com

Problem Reference:
    https://leetcode.com/problems/contains-duplicate/


"""
from typing import List
from unittest import TestCase


def contains_duplicate_one_liner(nums: List[int]) -> bool:
    """
    Uses Pythonic one-liner expression to determine if a list has any
    duplicate values.
    Args:
        nums: a list of integers

    Returns:
        True if duplicates exist else False
    """
    return len(set(nums)) < len(nums)


def contains_duplicate_manual(nums: List[int]) -> bool:
    """
    Given an integer array nums, return true if any value appears at least twice
    in the array, and return false if every element is distinct.
    Constraints:
        1 <= nums.length <= 10^5
        -10^9 <= nums[i] <= 10^9
    Args:
        nums: a list of integer values

    Returns:
        True if any value appears twice False if all distinct
    """
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


def contains_duplicate(nums: List[int]) -> bool:
    """
    Wrapper for whichever function is being tested.
    Args:
        nums: a list of integers

    Returns:
        True if duplicates else False
    """
    return contains_duplicate_one_liner(nums)


class TestContainsDuplicate(TestCase):
    """
    Runs a series of test cases on the contains duplicate function to assure
    that all outputs are expected values.
    """
    def test_case_1(self):
        nums = [1, 2, 3, 1]
        result = True
        self.assertTrue(contains_duplicate(nums) == result)

    def test_case_2(self):
        nums = [1, 2, 3, 4]
        result = False
        self.assertTrue(contains_duplicate(nums) == result)

    def test_case_3(self):
        nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
        result = True
        self.assertTrue(contains_duplicate(nums) == result)



