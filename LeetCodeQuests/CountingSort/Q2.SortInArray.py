from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def sift_down(i: int, heap_size: int) -> None:
            while True:
                left = 2 * i + 1
                right = 2 * i + 2
                largest = i

                if left < heap_size and nums[left] > nums[largest]:
                    largest = left
                if right < heap_size and nums[right] > nums[largest]:
                    largest = right

                if largest == i:
                    break

                nums[i], nums[largest] = nums[largest], nums[i]
                i = largest

        n = len(nums)
        if n <= 1:
            return nums

        for i in range((n // 2) - 1, -1, -1):
            sift_down(i, n)

        for end in range(n - 1, 0, -1):
            nums[0], nums[end] = nums[end], nums[0]
            sift_down(0, end)

        return nums

