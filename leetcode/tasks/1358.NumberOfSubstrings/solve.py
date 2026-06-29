class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        counter, left = 0, 0
        freq = {'a': 0, 'b': 0, 'c': 0}

        for right in range(len(s)):
            freq[s[right]] += 1
            while freq['a'] > 0 and freq['b'] > 0 and freq['c'] > 0:
                counter += len(s) - right
                freq[s[left]] -= 1
                left += 1

        return counter

# Runtime 108 ms, 49.34 %
# Memory 17.89 mb, 67.33 %
def main():
    solve = Solution()
    print(solve.numberOfSubstrings(s="abcabc"))
    print(solve.numberOfSubstrings(s="aaacb"))

if __name__ == '__main__':
    main()
