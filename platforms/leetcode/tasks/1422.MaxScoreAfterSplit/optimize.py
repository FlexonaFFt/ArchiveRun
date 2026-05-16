class Solution:
    def maxScore(self, s: str) -> int:
        max_score, n = 0, len(s)
        for i in range(1, n):
            left, right = s[:i], s[i:]
            zeros_in_left = left.count('0')
            ones_in_right = right.count('1')
            current_score = zeros_in_left + ones_in_right
            # print(f'{zeros_in_left} + {ones_in_right} = {current_score}')
            if current_score > max_score:
                max_score = current_score
        return max_score

# Runtime 3 ms, 49 %
# Memory 17.76 mb, 60.77 %
def main():
    solution = Solution()
    string1 = "011101"
    string2 = "00111"
    string3 = "1111"
    print(solution.maxScore(string1))
    print(solution.maxScore(string2))
    print(solution.maxScore(string3))

if __name__ == '__main__':
    main()
