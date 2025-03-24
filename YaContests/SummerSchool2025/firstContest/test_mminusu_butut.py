class Solution:
    def calculator(self, s: str) -> int:
        stack = []
        num, sign, ans = 0, 1, 0
        i = 0
        n = len(s)

        while i < n:
            char = s[i]
            if char.isdigit():
                num = 0
                while i < n and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                ans += sign * num
                num = 0
            elif char in "+-":
                if char == '-':
                    minus_count = 0
                    while i < n and s[i] == '-':
                        minus_count += 1
                        i += 1
                    sign = -1 if minus_count % 2 != 0 else 1
                else:
                    sign = 1
                    i += 1
            elif char == '(':
                stack.append((ans, sign))
                ans, sign = 0, 1
                i += 1
            elif char == ')':
                ans += sign * num
                num = 0
                prev_ans, prev_sign = stack.pop()
                ans = prev_ans + prev_sign * ans
                i += 1
            else:
                i += 1

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
    main()
