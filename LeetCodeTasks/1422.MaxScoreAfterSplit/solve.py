class Solution:
    def MaxScore(self, s: str) -> int:
        zeros, ones = 0, 0
        max_sum = 0
        for i in range(len(s)):
            left = s[:i]
            right = s[i:]
            for element in left:
                if element == '0':
                    zeros += 1
            for element in right:
                if element == '1':
                    ones += 1
            summa = zeros + ones
            zeros, ones = 0, 0
            max_sum = max(max_sum, summa)
        return max_sum


def main():
    solution = Solution()
    string = '011101'
    print(solution.MaxScore(string))

if __name__ == '__main__':
    main()
