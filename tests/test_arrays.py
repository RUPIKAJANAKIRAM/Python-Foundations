"""Tests for array patterns.

Note the shape of these: happy path, edge case, failure case. Copy that shape
for everything you add. If a function has no edge-case test, it isn't done.
"""

import pytest

from dsa.arrays import max_subarray_sum, two_sum


class TestTwoSum:
    @pytest.mark.parametrize(
        ("nums", "target", "expected"),
        [
            ([2, 7, 11, 15], 9, (0, 1)),
            ([3, 2, 4], 6, (1, 2)),
            ([3, 3], 6, (0, 1)),
            ([-1, -2, -3, -4], -6, (1, 3)),
        ],
    )
    def test_finds_pair(self, nums: list[int], target: int, expected: tuple[int, int]) -> None:
        assert two_sum(nums, target) == expected

    def test_returns_none_when_no_pair(self) -> None:
        assert two_sum([1, 2, 3], 100) is None

    def test_empty_input(self) -> None:
        assert two_sum([], 5) is None


class TestMaxSubarraySum:
    @pytest.mark.parametrize(
        ("nums", "expected"),
        [
            ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
            ([1], 1),
            ([5, 4, -1, 7, 8], 23),
            ([-3, -1, -2], -1),
        ],
    )
    def test_computes_max(self, nums: list[int], expected: int) -> None:
        assert max_subarray_sum(nums) == expected

    def test_empty_raises(self) -> None:
        with pytest.raises(ValueError, match="must not be empty"):
            max_subarray_sum([])
