"""Array and hash-map patterns.

Every function here follows the same contract, and so should everything you add:
a docstring stating the approach, time and space complexity, and full type hints.
Writing the complexity down forces you to actually know it.
"""


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
