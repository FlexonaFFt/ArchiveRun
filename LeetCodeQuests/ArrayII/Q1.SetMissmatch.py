class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        miss = match = -1
        freq = [0] * (len(nums) + 1)

        for x in nums: freq[x] += 1
        for i in range(1, len(nums) + 1):
            if freq[i] == 2: miss = i
            elif freq[i] == 0: match = i
        return [miss, match]
