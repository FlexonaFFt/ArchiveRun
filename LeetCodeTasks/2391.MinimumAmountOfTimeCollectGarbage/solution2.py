class Solution:
    def garbageCollection(self, garbage: list[str], travel: list[int]) -> int:
        met, ppr, gls, res = False, False, False, 0
        for iteration in garbage:
            res += len(iteration)

        for i in range(len(travel), 0, -1):
            met = met or "M" in garbage[i]
            ppr = ppr or "P" in garbage[i]
            gls = gls or "G" in garbage[i]
            res += travel[i - 1] * (met + ppr + gls)

        return res

# Runtime 35 ms, 88.42 %
# Memory 33.67 mb, 53.45 %
def main():
    solution = Solution()
    print(solution.garbageCollection(["G","P","GP","GG"], [2,4,3]))
    print(solution.garbageCollection(["MMM","PGM","GP"], [3,10]))

if __name__ == '__main__':
    main()
