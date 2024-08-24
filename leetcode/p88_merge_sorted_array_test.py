import pytest

from .p88_merge_sorted_array import Solution


@pytest.mark.parametrize(
    "nums1, m, nums2, n, answer",
    [
        ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6]),
        ([1], 1, [], 0, [1]),
        ([0], 0, [1], 1, [1]),
        ([2, 0], 1, [1], 1, [1, 2]),
        ([0, 0, 0, 0, 0], 0, [1, 2, 3, 4, 5], 5, [1, 2, 3, 4, 5]),
        ([-1, 0, 0, 3, 3, 3, 0, 0, 0], 6, [1, 2, 2], 3, [-1, 0, 0, 1, 2, 2, 3, 3, 3]),
    ],
)
def test_answers(nums1, m, nums2, n, answer):

    Solution().merge(
        nums1=nums1,
        m=m,
        nums2=nums2,
        n=n,
    )

    assert nums1 == answer
