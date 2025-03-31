class Solution:
    def putMarbles(self, weights: list[int], k: int) -> int:
        if k == 1:
            return 0

        pair_sums = []
        for i in range(len(weights) - 1):
            pair_sums.append(weights[i] + weights[i + 1])

        pair_sums.sort()

        min_score = sum(pair_sums[:k-1])
        max_score = sum(pair_sums[-(k-1):])

        return max_score - min_score

# Runtime 124 ms, 83.47 %
# Memory 30.48 mb, 29.34 %
def main():
    solve = Solution()
    print(solve.putMarbles(weights=[1,3,5,1], k=2))
    print(solve.putMarbles(weights=[1,3], k=2))

main()
