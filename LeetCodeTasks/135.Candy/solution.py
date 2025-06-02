class Solution:
    def candy(self, ratings: list[int]) -> int:
        n, counter = len(ratings), 0
        candies = [1] * n

        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        for i in range(n - 1, 0, -1):
            if ratings[i - 1] > ratings[i]:
                candies[i - 1] = max(candies[i] + 1, candies[i - 1])
            counter += candies[i - 1]
        return counter + candies[n - 1]

# Runtime 11 ms, 89.23 %
# Memory 19.96 mb, 36.16 %
def test():
    solution = Solution()
    print(solution.candy(ratings=[1,0,2]))
    print(solution.candy(ratings=[1,2,2]))

if __name__ == '__main__':
    test()
