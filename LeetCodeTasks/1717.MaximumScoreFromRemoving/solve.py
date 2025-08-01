class Solution:
    def maximumGain(self, s, x, y):
        def remove_substring(s, first, second, score):
            stack = []
            total = 0
            for c in s:
                if stack and stack[-1] == first and c == second:
                    stack.pop()
                    total += score
                else:
                    stack.append(c)
            return "".join(stack), total

        if x >= y:
            s, score1 = remove_substring(s, 'a', 'b', x)
            _, score2 = remove_substring(s, 'b', 'a', y)
        else:
            s, score1 = remove_substring(s, 'b', 'a', y)
            _, score2 = remove_substring(s, 'a', 'b', x)
        return score1 + score2


def test():
    solve = Solution()
    print(solve.maximumGain("cdbcbbaaabab",4,5))
    print(solve.maximumGain("aabbaaxybbaabb",5,4))

if __name__ == '__main__':
    test()
