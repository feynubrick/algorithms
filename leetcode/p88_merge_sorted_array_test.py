import pytest

from .p88_merge_sorted_array import Solution

@pytest.mark.parametrize("nums1, nums2, answer", [
    ([1,2,3,0,0,0], [2,5,6], [1,2,2,3,5,6]),
    ([1], [], [1]),
    ([0], [1], [1]),
    ([2,0], [1], [1,2]),
    ([0,0,0,0,0], [1,2,3,4,5], [1,2,3,4,5])
])
def test_answers(nums1, nums2, answer):

    Solution().merge(
        nums1=nums1,
        m=len([item for item in nums1 if item > 0]),
        nums2=nums2,
        n=len([item for item in nums2 if item > 0]),
    )

    assert nums1 == answer
    