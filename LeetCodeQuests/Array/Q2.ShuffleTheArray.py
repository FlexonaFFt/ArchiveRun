class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        answer = []
        for i in range(n):
            x = nums[i]
            y = nums[i + n]
            answer.append(x)
            answer.append(y)
        return answer
