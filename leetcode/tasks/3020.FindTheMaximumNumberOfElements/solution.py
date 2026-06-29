from typing import List
from collections import Counter 

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        counters = Counter(nums)
        output = 1

        # Посчитаем кол-во единиц, так как 
        # Единицы не дают пользы 
        if 1 in nums: 
            count_of_ones = counters[1]
            if count_of_ones % 2 == 1:
                output = max(output, count_of_ones)
            else: output = max(output, count_of_ones - 1)

        # Далее проходимся основным циклом
        for curr in counters:
            if curr == 1: continue
            
            current, length = curr, 0
            while counters[current] >= 2:
                length += 2
                current *= current
            if counters[current] >= 1:
                length += 1
            else: length -= 1
            output = max(output, length)

        return output 
