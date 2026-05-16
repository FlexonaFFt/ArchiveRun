class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        max_val = current = ans = 0
        for num in nums:
            if max_val < num:
                max_val = num 
                ans = current = 0
            
            if max_val == num:
                current += 1
            else: 
                current = 0

            ans = max(ans, current)

        return ans 


def test():
    solve = Solution()
    print(solve.longestSubarray(nums=[1,2,3,3,2,2]))
    print(solve.longestSubarray(nums=[1,2,3,4]))

if __name__ == '__main__':
    test()
