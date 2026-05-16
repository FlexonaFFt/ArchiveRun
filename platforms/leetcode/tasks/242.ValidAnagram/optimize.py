class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_s = sorted(s)
        sorted_t = sorted(t)
        return sorted_s == sorted_t

# Runtime 15 ms, 45 %
# Memory 18.68 mb, 11.67 %
def main():
    solution = Solution()
    print(solution.isAnagram(s="anagram", t="nagaram"))
    print(solution.isAnagram(s="rat", t="car"))

if __name__ == '__main__':
    main()
