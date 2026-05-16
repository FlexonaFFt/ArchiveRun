class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set, left, max_length = set(), 0, 0
        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)
        return max_length

# Runtime 17 ms, 65.5 %
# Memory 17.75 mb, 58 %
def main():
    string1 = "abcabcbb"
    string2 = "bbbbb"
    string3 = "pwwkew"
    solve = Solution()
    print(solve.lengthOfLongestSubstring(string1))
    print(solve.lengthOfLongestSubstring(string2))
    print(solve.lengthOfLongestSubstring(string3))

if __name__ == '__main__':
    main()
