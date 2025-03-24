class Solution:
    def calculator(self, s: str) -> int:
        stack = []
        num, sign, ans = 0, 1, 0

        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
            elif char in "+-":
                ans += sign * num
                num = 0
                sign = 1 if char == "+" else -1
            elif char == '(':
                stack.append((ans, sign))
                ans, sign = 0, 1
            elif char == ')':
                ans += sign * num
                num = 0
                prev_ans, prev_sign = stack.pop()
                ans = prev_ans + prev_sign * ans

        ans += sign * num
        return ans


def test():
    solution = Solution()
    print(solution.calculator("-123 + 23"))
    print(solution.calculator("-((5 -2) - (3) +2) + 1"))
    print(solution.calculator("(1 + -2) + (3-4 - (5-6 - 7)) +8"))
    print(solution.calculator("--42"))


def main():
    solution = Solution()
    string = input()
    print(solution.calculator(s=string))

if __name__ == "__main__":
    test()
