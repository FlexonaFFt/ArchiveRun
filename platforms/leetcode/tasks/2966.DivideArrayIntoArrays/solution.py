class Solution:
    def divideArray(self, nums: list[int], k: int) -> list[list[int]]:
        nums.sort()
        answer = []
        for i in range(0, len(nums), 3):
            if nums[i + 2] - nums[i] > k: return []
            answer.append([nums[i], nums[i + 1], nums[i + 2]])
        return answer

# Runtime 80 ms, 63.29 %
# Memory 33.56 mb, 12.24 %
def test():
    solve = Solution()
    print(solve.divideArray(nums=[1,3,4,8,7,9,3,5,1], k=2))
    print(solve.divideArray(nums=[2,4,2,2,5,2], k=2))

if __name__ == '__main__': test()
