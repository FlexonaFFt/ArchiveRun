class Solution:
    def countSubstrings(self, s: str) -> int:
        def is_palindrome(substring: str) -> bool:
            return substring == substring[::-1]

        count = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if is_palindrome(s[i:j+1]):
                    count += 1
        return count

# Runtime 769 ms, 6.49 %
# Memory 17.91 mb, 34.16 %
def main():
    solution = Solution()
    print(solution.countSubstrings(s='abc'))
    print(solution.countSubstrings(s='aaa'))

if __name__ == '__main__':
    main()
