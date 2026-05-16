class Solution:
    def longestPalindrome(self, string: str) -> int:
        charCounter = {}
        for char in string:
            if char not in charCounter:
                charCounter[char] = 1
            else:
                charCounter[char] += 1

        def findPalindrome(chars):
            length, odd_found = 0, False
            for count in chars.values():
                if count % 2 == 0:
                    length += count
                else:
                    length += count - 1
                    odd_found = True
            if odd_found:
                length += 1
            return length

        return findPalindrome(chars=charCounter)

# Runtime 0 ms, 100 %
# Memory 17.69 mb, 66.8 %
def main():
    solution = Solution()
    test1, test2 = "abccccdd", "a"
    print(solution.longestPalindrome(test1))
    print(solution.longestPalindrome(test2))

if __name__ == "__main__":
    main()
