class Solution:
    def partitionString(self, s: str) -> int:
        ans, ls = 1, []
        for i in s:
            if i in ls:
                ls = [i]
                ans += 1
            ls += [i]
        return ans


def main():
    solution = Solution()
    print(solution.partitionString(s='abacaba'))
    print(solution.partitionString(s="ssssss"))

main()
