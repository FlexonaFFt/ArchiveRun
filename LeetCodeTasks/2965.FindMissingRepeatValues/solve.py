class Solution:
    from typing import List
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n, counter = len(grid), {}
        for row in grid:
            for element in row:
                counter[element] = counter.get(element, 0) + 1

        for num in range(1, n * n + 1):
            if num not in counter:
                missing = num
            elif counter[num] == 2:
                repeat = num

        return [repeat, missing] # type: ignore

# Runtime 11 ms, 46.96 %
# Memory 18.31 mb, 23.37 %
def main():
    solution = Solution()
    print(solution.findMissingAndRepeatedValues(grid=[[1,3],[2,2]]))
    print(solution.findMissingAndRepeatedValues(grid=[[9,1,7],[8,9,2],[3,4,6]]))

if __name__ == '__main__':
    main()
