from typing import List 

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        
        nums = []
        for start in range(1, 9):

            num = start
            while num % 10 < 9:
                num = num * 10 + (num % 10 + 1)
                nums.append(num)

        return sorted(n for n in nums if low <= n <= high)
