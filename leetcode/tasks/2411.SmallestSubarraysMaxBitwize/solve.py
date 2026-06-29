class Solution:
    def smallestSubarrays(self, nums: list[int]) -> list[int]:
        answer, last = [1] * len(nums), [0] * 32
        for i in range(len(nums) - 1, -1, -1):
            for b in range(32):
                if nums[i] & (1 << b): last[b] = i
            
            max_len = 1
            for b in range(32):
                if last[b]: max_len = max(max_len, last[b] - i + 1)
            answer[i] = max_len

        return answer 


def test():
    solve = Solution()
    print(solve.smallestSubarrays(nums=[1,0,2,1,3]))
    print(solve.smallestSubarrays(nums=[1,2]))

if __name__ == '__main__':
    test()
