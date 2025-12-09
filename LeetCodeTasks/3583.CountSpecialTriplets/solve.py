from collections import Counter
from typing import List

class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        total, left = Counter(nums), Counter()
        counter, mod = 0, 10**9 + 7

        for num in nums:
            target = num * 2
            total[num] -= 1
            l, r = left.get(target, 0), total.get(target, 0)

            if l >= 1 and r >= 1:
                counter = (counter + l * r) % mod
            left[num] += 1
        
        return counter
