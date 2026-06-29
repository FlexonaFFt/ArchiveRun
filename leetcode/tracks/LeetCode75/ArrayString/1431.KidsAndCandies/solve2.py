class Solution:
    from typing import List 
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        return [candy + extraCandies >= max_candies for candy in candies]

# Memory: 17.44 mb, 58.44 %
def main():
    solution = Solution()
    cand_list, extras = [2, 3, 5, 1, 3], 3
    print(solution.kidsWithCandies(candies=cand_list, extraCandies=extras))

if __name__ == '__main__':
    main()
