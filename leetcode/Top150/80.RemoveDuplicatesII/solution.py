'''
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        write = 0

        for num in nums:
            if write < 2 or num != nums[write - 2]:
                nums[write] = num
                write += 1

        return write

'''

# Мое решение через словарик
from typing import List
from collections import Counter

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        counter, i = Counter(nums), 0

        for key, value in counter.items():
            if value > 2: counter[key] = 2

        for key, value in counter.items():
            for _ in range(value):
                nums[i] = key
                i += 1

        return i
