class Solution:
    from typing import List 
    def increasingTriplet(self, nums: List[int]) -> bool:
        first, second = float('inf'), float('inf')
        for num in nums:
            if num <= first:
                first = num 
            elif num <= second:
                second = num 
            else:
                return True 
        return False 

# Runtime 19 ms, 41.29 %
# Memory 37.42 mb, 36.28 %
def main():
    chisla = list(map(int, input().split()))
    solve = Solution()
    print(solve.increasingTriplet(nums=chisla))

if __name__ == '__main__':
    main()
