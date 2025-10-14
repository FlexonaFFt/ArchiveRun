class Solution:
    def hasIncreasingSubarrays(self, nums: list[int], k: int) -> bool:
        counter, current, length = 0, 0, 0
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                current += 1

            else:
                counter = current
                current = 1

            length = max(length, counter)
        if length >= k:
            return True 
        else: return False 


def test():
    solve = Solution()
    print(solve.hasIncreasingSubarrays([2,5,7,8,9,2,3,4,3,1], 3))
    print(solve.hasIncreasingSubarrays([1,2,3,4,4,4,4,5,6,7], 5))


if __name__ == '__main__':
    test()
