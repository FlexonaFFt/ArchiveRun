class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_index = 0
        t_index = 0
        while t_index < len(t):
            if s_index < len(s) and s[s_index] == t[t_index]:
                s_index += 1
            t_index += 1
        return s_index == len(s)

# Runtime 1 md, 40 %
# Memory 17.79 mb, 37.56 %
def main():
    input_ = str(input())
    podstroka = str(input())
    solution = Solution()
    print(solution.isSubsequence(input_, podstroka))

if __name__ == '__main__':
    main()
