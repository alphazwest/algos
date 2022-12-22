"""
From Here:
    https://leetcode.com/problems/longest-substring-without-repeating-characters/solutions/
"""
import logging
from collections import Counter
logging.getLogger().setLevel(logging.INFO)


def longest_substring_one(s: str) -> int:
    """
    Brute Force approach.
    Complexity:
        O(n^3)
    """
    def check(start, end):
        logging.info(f'check: {start} - {end}')
        chars = set()

        # O(n)
        for i in range(start, end + 1):  # inclusive
            if s[i] in chars:
                logging.info(f'{s[i]} in chars. Return False')
                return False
            logging.info(f'{s[i]} not in chars <{chars}> for index: [{i}]')
            chars.add(s[i])
            logging.info(f'Updated Chars: {chars}')
        return True

    n = len(s)
    result = 0
    # O(n)
    for i in range(n):
        # O(n)
        for j in range(i, n):
            if check(i, j):
                result = max(result, j-i+1)
                logging.info(f'New Result: {result}')
    return result


def longest_substring_two(string: str) -> int:
    """
    Calculates the length of the longest substring of sequential unique
    characters.
    """
    # hashmap for the characters
    chars = {}

    # sliding window bounds' pointers
    left = 0
    right = 0

    # the final result
    result = 0

    # until the right pointer hits the furthest character
    while right < len(string):
        r = string[right]
        logging.info(f'r: {r}')

        # either add or increment
        if r in chars:
            chars[r] += 1
        else:
            chars[r] = 1
        logging.info(f'chars[r] += 1: {chars}')

        # moves the left pointer right until
        while chars[r] > 1:
            l = string[left]
            logging.info(f'l: {l}')
            if l in chars:
                chars[l] -= 1
            else:
                chars[l] = 0
            logging.info(f'chars[l] -= 1: {chars}')
            left += 1
            logging.info(f'Left Update: {left}')

        result = max(result, right - left + 1)
        logging.info(f'Result: {result}')

        right += 1
        logging.info(f'Right Update: {right}')
    return result


def longest_substring_two_counter(string: str) -> int:
    """
    Calculates the length of the longest substring of sequential unique
    characters.
    O(2n) == O(n). Worst case, each letter visited twice.
    """
    # the O(n) iterator
    _i = 0

    # define the hash-mapping for the character accounting
    chars = Counter()

    # defines the pointers of either side of the sliding window
    left = right = 0

    res = 0
    while right < len(string):
        _i += 1  # stats counter
        r = string[right]
        chars[r] += 1

        # when duplicate character found, increments the left side
        # of the sliding window to the index of the right
        while chars[r] > 1:
            _i += 1
            l = string[left]
            chars[l] -= 1
            left += 1

        # the result is the length of the window
        res = max(res, right - left + 1)

        right += 1
    logging.info(f'iterations: {_i}. n: {len(string)}')
    return res


def longest_substring_optimized(string: str) -> int:
    """
    Similar to the Counter method but instead stores a mapping from
    character to index such that there is no looping to re-adjust
    the leftmost window pointer.
    Time: O(n)
    Space: O(min(m, n))  # n = size of string, m = possible character set
    """
    # performance iterator
    _i = 0

    n = len(string)
    result = 0
    charmap = {}

    i = 0
    for j in range(n):
        _i += 1

        # get the next character
        c = string[j]

        # check if duplicate
        if c in charmap:

            # if duplicate, update i value
            i = max(charmap[c], i)
            # Case 1: i < charmap[c] - first duplicate character
            # Case 2: i > charmap[c] - not first duplicate character

        # keep largest result
        result = max(result, j - i + 1)
        # Case 1: result

        # update charmap value of last character to current functional position
        charmap[c] = j + 1

    logging.info(f'iterations: {_i}. n: {len(string)}')
    return result



def az_custom(string: str) -> int:
    """
    Implementing from memory
    1.2
    """
    _i = 0
    # accountancy for character position
    char_map = {}

    # initial result
    result = 0

    # left slider pointer
    i = 0

    for j in range(len(string)):
        _i += 1

        if string[j] in char_map:

            i = max(char_map[string[j]], i)

        # result is max of last max or size
        # of current window width.
        result = max(result, j-i + 1)

        # update character value to current char
        char_map[string[j]] = j + 1

    logging.info(f'n: {len(string)}. Iterations: {i}.')
    return result







def longest_substring(string: str) -> int:
    """
    Given a string, finds the longest substring without repeating chars.
    Args:
        string:

    Returns:

    """
    return az_custom(string=string)


if __name__ == "__main__":

    _1 = "abccdeeeffdsdafsdfvxcvsdfs"     # 3
    _2 = "bbbbb"        # 1
    _3 = "pwwkew"       # 3

    print(longest_substring(_1))
    # print(longest_substring(_2))
    # print(longest_substring(_3))