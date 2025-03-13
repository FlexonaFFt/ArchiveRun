class Solution:
    def minZeroArray(self, nums: list[int], queries: list[list[int]]) -> int:
        n, m, q = len(nums), len(queries), queries[::-1]
        delta, current_sum = [0] * (n + 1), 0

        for i, num in enumerate(nums):
            current_sum += delta[i]
            while q and current_sum < num:
                start, end, val = q.pop()
                if end >= i:
                    if start <= i:
                        current_sum += val
                    else: delta[start] += val
                    delta[end + 1] -= val
            if current_sum < num:
                return -1
        return m - len(q)

# Runtime 79 ms, 100 %
# Memory 64.28 mb, 23.15 %
def main():
    solution = Solution()
    print(solution.minZeroArray([2,0,2], [[0,2,1],[0,2,1],[1,1,3]]))
    print(solution.minZeroArray([4,3,2,1], [[1,3,2],[0,2,1]]))

if __name__ == '__main__':
    main()
