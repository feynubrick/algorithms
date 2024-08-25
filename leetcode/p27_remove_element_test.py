import pytest

from .p27_remove_element import Solution


@pytest.mark.parametrize(
    "nums, val, answer, k",
    [
        ([3, 2, 2, 3], 3, [2, 2], 2),
        ([0, 1, 2, 2, 3, 0, 4, 2], 2, [0, 0, 1, 3, 4], 5),
    ],
)
def test_answers(nums, val, answer, k):
    return_val = Solution().removeElement(nums, val)
    assert return_val == k
    for nums_item, answer_item in zip(sorted(nums[:k]), answer):
        assert nums_item == answer_item
