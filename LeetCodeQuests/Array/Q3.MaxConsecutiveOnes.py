class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxCounter = counter = 0
        for element in nums:
            if element == 1:
                counter += 1
            else: counter = 0
            
            if counter > maxCounter:
                maxCounter = counter

        return maxCounter
