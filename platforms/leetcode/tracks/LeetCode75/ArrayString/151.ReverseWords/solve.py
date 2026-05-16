class Solution:
    def reverseWords(self, string: str) -> str:
        words_list = string.split()
        words_list.reverse()
        return ' '.join(words_list)

# Runtime 0 ms, 100 %
# Memory 17.95 mb, 23.16 %
def main():
    string = "the sky is blue"
    solution = Solution()
    print(solution.reverseWords(string=string))

if __name__ == '__main__':
    main()
