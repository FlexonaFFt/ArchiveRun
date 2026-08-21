'''
Даны два массива: [1, 2, 3, 2, 0] и [5, 1, 2, 7, 3, 2]
Надо вернуть [1, 2, 2, 3] (порядок неважен)
'''

class Solution:

    def checker(self, nums1: list[int], nums2: list[int]):
        counter, out = {}, [] 

        for num in nums1: 
            counter[num] = counter.get(num, 0) + 1
        for num in nums2: 
            count = counter.get(num, 0)
            if count > 0: 
                out.append(num)
                counter[num] -= 1

        return out
