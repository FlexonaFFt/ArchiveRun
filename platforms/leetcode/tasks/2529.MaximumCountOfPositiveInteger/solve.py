class Solution:
    from typing import List
    def maximumCount(self, nums: List[int]) -> int:
        positive, negative = 0, 0
        for element in nums:
            if element > 0:
                positive += 1
            elif element < 0:
                negative += 1
        if positive > negative:
            return positive
        return negative

# Runtime 2 ms, 36.21 %
# Memory 18.00 mb, 69.11 %
def main():
    solve = Solution()
    print(solve.maximumCount(nums=[-2,-1,-1,1,2,3]))
    print(solve.maximumCount(nums=[-3,-2,-1,0,0,1,2]))
    print(solve.maximumCount(nums=[5,20,66,1314]))

if __name__ == '__main__':
    main()
