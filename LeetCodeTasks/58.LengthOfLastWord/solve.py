class Solution:
    def lengthOfLastWord(self, string: str) -> int:
        string = string.strip().split(" ") # type: ignore
        return len(string[-1]) 

# Runtime 0 ms, Beats 100 %
# Memory 17.6 mb, Beats 42.09 %
def main():
    string = "   fly me   to   the moon  "
    solution = Solution()
    print(solution.lengthOfLastWord(string=string))

if __name__ == '__main__':
    main()
