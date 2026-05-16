class Solution:
    from typing import List
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n, res = len(nums), []
        for i in range(n):
            if nums[i][i] == '0':
                res.append('1')
            else:
                res.append('0')
        return ''.join(res)

# Runtime 0 ms, 100 %
# Memory 17.92 mb, 31.88 %
def main():
    solve = Solution()
    print(solve.findDifferentBinaryString(nums=["01","10"]))
    print(solve.findDifferentBinaryString(nums=["00","01"]))
    print(solve.findDifferentBinaryString(nums=["111","011","001"]))

if __name__ == '__main__':
    main()
