from typing import List

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total_mod = sum(nums) % p
        if total_mod == 0: return 0
        
        last_pos, prefix, answer = {0: -1}, 0, len(nums)
        for i, x in enumerate(nums):
            prefix = (prefix + x) % p
            need = (prefix - total_mod) % p

            if need in last_pos:
                length = i - last_pos[need]
                if length < answer: answer = length

            last_pos[prefix] = i
        return -1 if answer == len(nums) else answer
