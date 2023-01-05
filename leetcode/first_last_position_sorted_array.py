"""
Given an array of integer nums sorted in non-decreasing order,
find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.

From Here:
    https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
"""
import logging
from typing import List


def get_range(nums: List[int], target: int) -> List[int]:
    """
    Given a list of integers, in ascending order, and a target integer,
    find the range of indices within the nums that the target is found.
    If no target is found, returns the array [-1, -1].

    Notes:
        Approaches as a two-pointer problem in O(n) time.

    Constraints:
        0 <= nums.length <= 105
        -109 <= nums[i] <= 109
        nums is a non-decreasing array.
        -109 <= target <= 109

    Args:
        nums: a list of integers sorted in ascending value.
        target: the integer to search for

    Returns:
        List of two integers as [start, end] of the range, inclusive on both ends
    """
    # check some basic conditions
    if len(nums) == 0:
        return [-1, -1]
    if len(nums) == 1 and nums[0] == target:
        return [0, 0]

    # setup some iterators and initial values for range indices
    i = 0
    j = len(nums) - 1
    left = -1
    right = -1

    # debugging and stats only
    _i = 0

    # approach as a two-pointer problem with i from the left, j from the right
    while i <= j:  # break if the ends meet
        _i += 1

        logging.debug(f'iteration #{_i}: i={i} j={j}')
        logging.debug(f"nums[i]={nums[i]}; nums[j]={nums[j]}")

        # compare against target
        if nums[i] == target:
            logging.debug(f"target found for i = {i}: {nums[i]}")
            left = i
        else:
            logging.debug(f"i no match. incrementing i...")
            i += 1

        if nums[j] == target:
            logging.debug(f"target found for j = {j}: {nums[j]}")
            right = j
        else:
            logging.debug(f"j no match. decrementing j ...")
            j -= 1

        if left != -1 and right != -1:
            logging.debug(f"Break -- left: {left}; right: {right}")
            break

    logging.info(f'{len(nums)} total numbers checked in {_i} iterations.')
    return [left, right]


if __name__ == "__main__":

    logging.getLogger().setLevel(logging.INFO)

    print("1:", get_range(nums=[5, 7, 7, 8, 8, 10], target=8))
    # should be [3, 4]

    print("2:", get_range(nums=[5, 7, 7, 8, 8, 10], target=6))
    # should be [-1, -1]

    print("3:", get_range(nums=[], target=0))
    # should be [-1, -1]

    print("4:", get_range(nums=[1, 3], target=1))
    # should be [0, 0]

