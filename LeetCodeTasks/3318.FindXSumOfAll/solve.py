class Solution:
    def findXSum(self, nums: list[int], k: int, x: int) -> list[int]:
        if k <= 0 or k > len(nums): return []
        
        current_sum, answer = sum(nums[:k]), []
        answer.append(current_sum)
        for i in range(k, len(nums)):
            current_sum += nums[i]
            current_sum -= nums[i - k]
            answer.append(current_sum)
        
        return answer


def test():
    solve = Solution()
    print(solve.findXSum([1,1,2,2,3,4,2,3], 6, 2))
    print(solve.findXSum([3,8,7,8,7,5], 2, 2))

if __name__ == '__main__':
    test()
