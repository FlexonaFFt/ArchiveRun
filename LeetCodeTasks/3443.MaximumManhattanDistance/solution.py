class Solution:
    def count(self, drt1: int, drt2: int, times: int) -> int:
        return (
            abs(drt1 - drt2) + times * 2
        )

    def maxDistance(self, s: str, k: int) -> int:

        ans = 0
        north = south = east = west = 0
        for it in s:
            if it == 'N': north += 1
            if it == 'S': south += 1
            if it == 'E': east += 1
            if it == 'W': west += 1
            times1 = min(north, south, k)
            times2 = min(east, west, k - times1)
            ans = max(ans, self.count(north, south, times1) + self.count(east, west, times2))

        return ans

# Runtime 2602 ms, 65.63 %
# Memory 18.13 mb, 37.50 %
def test():
    solve = Solution()
    print(solve.maxDistance("NWSE", 1))
    print(solve.maxDistance("NSWWEW", 3))

if __name__ == '__main__': test()
