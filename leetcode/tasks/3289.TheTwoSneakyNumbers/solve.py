class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        counter, result = [], []
        for num in nums:
            if num not in counter: counter.append(num)
            else: result.append(num)

        return result
