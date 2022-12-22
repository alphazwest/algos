"""
From here:
https://leetcode.com/problems/two-sum/solutions/127810/two-sum/
"""
from typing import List


def brute_force(nums, target):
    """
    O(n^2) complexity -- not great.
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j:
                if nums[i] + nums[j] == target:
                    return [i, j]
    return []


def two_pass_hash_table(nums, target):
    """
    Creates a hashmap as [num, index] then checks the compliment of
    each entry against the target, checking if that compliment is
    in the hashmap. If it is, and not equal to the current iterator,
    return the indices.
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    hash_map = {}

    for i, num in enumerate(nums):
        hash_map[num] = i

    for i, num in enumerate(nums):

        compliment = target - num
        if compliment in hash_map and hash_map[compliment] != i:
            return [i, hash_map[compliment]]


def single_pass_hash_table(nums, target):
    """
    Time Complexity: O(n)
    Space Complexity: O(n)
    Conceptually better, though not by an order of magnitude.
    """
    hash_map = {}
    for i, num in enumerate(nums):
        compliment = target - num
        if compliment in hash_map:
            return [i, hash_map[compliment]]

        # add the number after checking for the compliment
        hash_map[num] = i


def two_sum(nums: List[int], target: int) -> List[int]:
    """
    Given an array of integers nums and an integer target, return indices of the two
    numbers such that they add up to target. You may assume that each input would
    have exactly one solution, and you may not use the same element twice. You can
    return the answer in any order.
    """
    return single_pass_hash_table(nums=nums, target=target)


if __name__ == "__main__":

    print(two_sum(nums=[2, 7, 11, 15], target=9))

    print(two_sum(nums=[3, 2, 4], target=6))

    print(two_sum(nums=[3, 3], target=6))

