class Solution:
    from typing import List
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        index = {x: i for i, x in enumerate(arr)}
        max_len, n, dp = 0, len(arr), {}

        for i in range(n):
            for j in range(i + 1, n):
                x = arr[j] - arr[i]
                if x in index and index[x] < i:
                    k = index[x]
                    dp[(i, j)] = dp.get((k, i), 2) + 1
                    max_len = max(max_len, dp[(i, j)])
        return max_len if max_len >= 3 else 0

# Runtime 717 ms, 80.80 %
# Memory 18.39 mb, 55.96 %
def main():
    solution = Solution()
    print(solution.lenLongestFibSubseq(arr=[1,2,3,4,5,6,7,8]))
    print(solution.lenLongestFibSubseq(arr=[1,3,7,11,12,14,18]))

if __name__ == '__main__':
    main()
