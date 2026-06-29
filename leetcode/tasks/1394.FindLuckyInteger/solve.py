from collections import Counter 

class Solution:
    def findLucky(self, arr: list[int]) -> int:
        max_cnt = -1
        for x, f in Counter(arr).items():
            if x == f: max_cnt = max(x, max_cnt)

        return max_cnt 

# Runtime 0 ms, 100 %
# Memory 17.94 mb, 31.09 %
def test():
    solve = Solution()
    print(solve.findLucky(arr=[2,2,3,4]))
    print(solve.findLucky(arr=[1,2,2,3,3,3]))
    print(solve.findLucky(arr=[2,2,2,3,3]))


if __name__ == '__main__':
    test()
