"""Array and hash-map patterns.

Every function here follows the same contract, and so should everything you add:
a docstring stating the approach, time and space complexity, and full type hints.
Writing the complexity down forces you to actually know it.
"""

from collections import Counter


def two_sum(nums: list[int], target: int) -> tuple[int, int] | None:
    """Return indices of the two numbers adding to target, or None.

    Approach: one pass, storing each value's index in a dict as we go. For each
    number we ask whether its complement has already been seen.

    Time: O(n) — single pass, O(1) dict lookups.
    Space: O(n) — worst case every value is stored.
    """
    seen: dict[int, int] = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return (seen[complement], i)
        seen[num] = i
    return None


def max_subarray_sum(nums: list[int]) -> int:
    """Return the largest sum of any contiguous non-empty subarray (Kadane's).

    Approach: at each element, either extend the running subarray or start fresh
    from the current element, whichever is larger. Track the best seen.

    Time: O(n). Space: O(1).
    """
    if not nums:
        raise ValueError("nums must not be empty")

    best = current = nums[0]
    for num in nums[1:]:
        current = max(num, current + num)
        best = max(best, current)
    return best


def contains_duplicate(nums: list[int]) -> bool:
    """Return True if any value appears at least twice.

    https://leetcode.com/problems/contains-duplicate/

    Approach: track seen values in a set; a value already present means a
    duplicate. Returns early on the first collision.

    Time: O(n) — one pass, O(1) set membership.
    Space: O(n) — worst case all values distinct and stored.
    """
    seen: set[int] = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    counts: dict[str, int] = {}
    for char in s:
        counts[char] = counts.get(char, 0) + 1

    for char in t:
        if char not in counts:
            return False
        counts[char] -= 1
        if counts[char] == 0:
            del counts[char]

    return not counts


def group_anagrams(strs: list[str]) -> list[list[str]]:
    groups: dict[tuple[str, ...], list[str]] = {}
    for s in strs:
        key = tuple(sorted(s))
        if key not in groups:
            groups[key] = []
        groups[key].append(s)

    return list(groups.values())


def top_k_frequent(nums: list[int], k: int) -> list[int]:
    return [n for n, _ in Counter(nums).most_common()][:k]


def product_except_self(nums: list[int]) -> list[int]:
    """Return an array where each index holds the product of all other numbers."""
    n = len(nums)
    result = [1] * n

    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]

    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]

    return result
