class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        answer = []
        for i in range(len(nums)):
            localCounter = 0
            for j in range(len(nums)):
                if nums[j] != nums[i]:
                    if nums[i] > nums[j]:
                        localCounter += 1
                else: continue
            answer.append(localCounter)
            localCounter = 0
        return answer
