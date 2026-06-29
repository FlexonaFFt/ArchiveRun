class Solution:
    from typing import List
    def diffWaysToCompute(self, expression: str) -> List[int]:
        if expression.isdigit():
            return [int(expression)]
        ans = []
        for i, char in enumerate(expression):
            if char in {'+', '-', '*'}:
                left_res = self.diffWaysToCompute(expression[:i])
                right_res = self.diffWaysToCompute(expression[i+1:])
                for left in left_res:
                    for right in right_res:
                        if char == '+':
                            ans.append(left + right)
                        elif char == '-':
                            ans.append(left - right)
                        elif char == '*':
                            ans.append(left * right)
        return ans

# Runtime 3 ms, 54.17 %
# Memory 17.93 mb, 35.96 %
def main():
    solution = Solution()
    print(solution.diffWaysToCompute(expression="2-1-1"))
    print(solution.diffWaysToCompute(expression="2*3-4*5"))

if __name__ == '__main__':
    main()
