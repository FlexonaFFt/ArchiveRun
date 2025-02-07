class Solution:
    def firstUniqChar(self, s: str) -> int:
        chars = {}
        for element in s:
            if element not in chars:
                chars[element] = 1
            else:
                chars[element] += 1
        for index, char in enumerate(s):
            if chars[char] == 1:
                return index
        return -1

# Runtime 74 ms, 32.04 %
# Memory 18.08 mb, 48.37 %
def main():
    solve = Solution()
    print(solve.firstUniqChar("leetcode"))
    print(solve.firstUniqChar("loveleetcode"))
    print(solve.firstUniqChar("aabb"))

if __name__ == '__main__':
    main()
