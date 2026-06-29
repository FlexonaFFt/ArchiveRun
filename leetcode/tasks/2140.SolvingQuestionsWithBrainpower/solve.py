class Solution(object):
    def mostPoints(self, questions):
        dp = [0] * len(questions)
        for i in range(len(questions) - 1, -1, -1):
            index = i + questions[i][1] + 1
            if index < len(questions):
                dp[i] = dp[index] + questions[i][0]
            else:
                dp[i] = questions[i][0]
            if i < len(questions) - 1:
                dp[i] = max(dp[i + 1], dp[i])
        return dp[0]


def main():
    solve = Solution()
    print(solve.mostPoints(questions=[[3,2],[4,3],[4,4],[2,5]]))
    print(solve.mostPoints(questions=[[1,1],[2,2],[3,3],[4,4],[5,5]]))

main()
