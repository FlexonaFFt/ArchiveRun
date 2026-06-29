from collections import Counter
class Solution:
    def maxDifference(self, s: str) -> int:
        c = Counter(s)
        maxOdd = max(x for x in c.values() if x % 2 == 1)
        minEven = min(x for x in c.values() if x % 2 == 0)
        return maxOdd - minEven


def main():
    solution = Solution()
    print(solution.maxDifference(s="aaaaabbc"))
    print(solution.maxDifference(s="abcabcab"))

if __name__ == '__main__': main()
