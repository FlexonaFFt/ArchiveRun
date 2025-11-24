from typing import List

class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        total_even = 0
        total_odd = 0
        for i, val in enumerate(nums):
            if i % 2 == 0:
                total_even += val
            else:
                total_odd += val
        left_even = 0
        left_odd = 0
        answer = 0

        for i, val in enumerate(nums):
            right_even_before = total_even - (val if i % 2 == 0 else 0)
            right_odd_before = total_odd - (val if i % 2 == 1 else 0)

            right_even_after = right_odd_before  
            right_odd_after = right_even_before  
            even_sum_after = left_even + right_even_after
            odd_sum_after = left_odd + right_odd_after

            if even_sum_after == odd_sum_after:
                answer += 1
            if i % 2 == 0:
                left_even += val
                total_even -= val  
            else:
                left_odd += val
                total_odd -= val   

        return answer

