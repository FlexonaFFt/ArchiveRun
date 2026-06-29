class Solution:
    def countMaxOrSubsets(self, nums: list[int]) -> int:
        n, maxOr, count = len(nums), 0, 0
        for num in nums: maxOr |= num
        for mask in range(1, 1 << n):
            current = 0
            for i in range(n):
                if mask & (1 << i): current |= nums[i]
            if current == maxOr: count += 1
        return count

def test():
    solve = Solution()
    print(solve.countMaxOrSubsets(nums=[3,1]))
    print(solve.countMaxOrSubsets(nums=[2,2,2]))
    print(solve.countMaxOrSubsets(nums=[3,2,1,5]))

if __name__ == '__main__':
    test()

