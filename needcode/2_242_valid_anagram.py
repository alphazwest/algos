"""
NeetCode.io problem #2 from arrays.
References LeetCode.com problem # 242 here:
    https://leetcode.com/problems/valid-anagram/
"""
from collections import Counter
from unittest import TestCase


def valid_anagram_python(s: str, t: str) -> bool:
    """
    Function to determine if <t> contains a valid anagram of <a> using the
    Counter class which is, practically, like cheating.
    Args:
        s: characters considered essential to being anagram.
        t: the characters in which an anagram may be contained.

    Returns:

    """
    return Counter(s) == Counter(t)


def valid_anagram_dicts(s: str, t: str) -> bool:
    """
    Use hashmap to determine if all characters in s are in t such that it can
    be said tha t is an anagram of s.
    Args:
        s: character sequence a-z
        t: character sequence a-z

    Returns:
        True if all chars in s in t and len(s) == len(t)
    """
    # case where extra letters are present
    if len(s) != len(t):
        return False

    # create mapping of characters from s
    charmap = {}
    for char in s:
        # initialize new values to 0
        if char not in charmap:
            charmap[char] = 0
        # increment all values as seen
        charmap[char] += 1

    # for each char in t, decrement the count of the character added from s.
    # if, at any point in time, a character not in <s> is detected, return False
    for char in t:
        if char not in charmap:
            return False
        charmap[char] -= 1

    # confirm that all characters are seen in equivalent counts
    for char, count in charmap.items():
        if count != 0:
            return False
    return True


def valid_anagram(s: str, t: str) -> bool:
    """
    Given two strings s and t, return true if t is an anagram of s, and
    false otherwise.

    An Anagram is a word or phrase formed by rearranging the letters of a
    different word or phrase, typically using all the original letters exactly
    once.
    Args:
        s: the <potentially> smaller word of letters to deem necessary.
        t: the <potentially> larger set of characters from which an anagram
            can be determined.

    Returns:
        True if each element in a is found in element b
    """
    # where all letters couldn't possibly be contained
    if len(s) != len(t):
        return False

    # create some counters for a-z lowercase
    counts_s = [0] * 26
    counts_t = [0] * 26

    for i in range(len(s)):
        # get + subtract ordinal values to map to count's arrays
        counts_s[ord(s[i]) - ord("a")] += 1
        counts_t[ord(t[i]) - ord("a")] += 1

    # compare each array to see that the same number of occurrences of
    # each character in a is found in b.
    for i in range(len(counts_s)):
        if counts_s[i] != counts_t[i]:
            return False

    return True


class TestValidAnagram(TestCase):

    def setUp(self) -> None:
        self.function = valid_anagram_dicts

    def test_case_1(self):
        self.assertEqual(self.function("anagram", "nagaram"), True)

    def test_case_2(self):
        self.assertEqual(self.function("rat", "car"), False)

    def test_case_3(self):
        self.assertEqual(self.function("a", "ab"), False)

    def test_case_4(self):
        self.assertEqual(self.function("aacc", "ccac"), False)


