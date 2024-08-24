from typing import List

"""
문제 출처: https://leetcode.com/problems/merge-sorted-array/description/

You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

 

Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].

Example 3:

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.

 

Constraints:

    nums1.length == m + n
    nums2.length == n
    0 <= m, n <= 200
    1 <= m + n <= 200
    -109 <= nums1[i], nums2[j] <= 109

 

Follow up: Can you come up with an algorithm that runs in O(m + n) time?

"""

class OldSolution:
    """
    나의 풀이를 분석해보자.

    시간 복잡도를 먼저 고려해보자.
    - 이중 루프에서 worst case는 n*m
    - insert item에서 worst case는 n+m
        - m 루프 하나에서 한번의 n+m이 발생
        - 따라서 big-O notaion으로 표현할 때는 더해야 함
    따라서 O(n*(m+n+m)) = O(n*m + n^2)
    n ~= m 이면, O((n+m)^2) 이다.
    좋지 않다.
    """
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            nums1.clear()

            for nums2_item in nums2:
                nums1.append(nums2_item)
            return

        nums1_index = 0

        for nums2_item in nums2:
            for i in range(nums1_index, m):
                compare_item = nums1[i]
                if nums2_item < compare_item:
                    nums1_index = i
                    self.insert_item(nums1, i, nums2_item)
                    m += 1
                    break

                if i == m - 1:
                    nums1[m] = nums2_item
                    m += 1

    @staticmethod
    def insert_item(nums: List[int], index: int, item: int):
        rest_items = nums[index:]
        nums[index] = item
        for i, rest_item in enumerate(rest_items):

            j = index + i + 1
            if j < len(nums):
                nums[j] = rest_item
            else:
                if rest_item > 0:
                    nums.append(rest_item)


class Solution:
    """
    이번에는 다르게 접근해보자. 포인트는 nums1, nums2가 모두 이미 정렬되어 있다는 것.
    메모리를 이용하면 될 듯하다.
    """

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if len(nums1) == 0:
            nums1.extend(nums2)

        if len(nums2) == 0:
            return
        
        merged = []
        i, j = 0, 0
        while i < m + n and j < n:
            if nums1[i] == 0:
                merged.append(nums2[j])
                j += 1
            elif nums1[i] <= nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])

        nums1.clear()
        nums1.extend(merged)
