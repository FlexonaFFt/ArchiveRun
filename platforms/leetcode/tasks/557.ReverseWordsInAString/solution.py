class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        reversedWords = [word[::-1] for word in words]
        return ' '.join(reversedWords)

# Runtime 0 ms, 100 %
# Memory 18.56 mb, 28.20 %
def main():
    solution = Solution()
    print(solution.reverseWords(s="Let's take LeetCode contest"))
    print(solution.reverseWords(s="Mr Ding"))

if __name__ == '__main__':
    main()
