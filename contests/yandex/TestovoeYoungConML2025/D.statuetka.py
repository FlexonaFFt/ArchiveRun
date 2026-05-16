class Solution:
    def solve(self, n: int, k: int, a: list):
        from collections import defaultdict
        count, min_cost = defaultdict(int), float('inf')
        left, types, total_cost = 0, 0, 0

        for right in range(n):
            val = a[right]
            total_cost += val
            if 1 <= val <= k:
                count[val] += 1
                if count[val] == 1: types += 1

            while types == k:
                min_cost = min(min_cost, total_cost)
                left_val = a[left]
                total_cost -= left_val
                if 1 <= left_val <= k:
                    count[left_val] -= 1
                    if count[left_val] == 0: types -= 1
                left += 1

        return min_cost



def test():
    solve = Solution()
    a1 = solve.solve(6, 3, [1,2,2,3,3,1])
    a2 = solve.solve(5, 3, [1,2,5,4,3])
    a3 = solve.solve(6, 3, [1,2,6,3,3,1])
    a4 = solve.solve(6, 1, [6,2,3,1,2,3])
    a5 = solve.solve(7, 7, [1,2,3,4,6,5,7])
    a6 = solve.solve(10, 2, [1,9,2,4,3,1,8,2,10,9])

    res1 = 8
    res2 = 15
    res3 = 12
    res4 = 1
    res5 = 28
    res6 = 10

    print(solve.solve(6, 3, [1,2,2,3,3,1]))
    print(solve.solve(5, 3, [1,2,5,4,3]))
    print(solve.solve(6, 3, [1,2,6,3,3,1]))
    print(solve.solve(6, 1, [6,2,3,1,2,3]))
    print(solve.solve(7, 7, [1,2,3,4,6,5,7]))
    print(solve.solve(10, 2, [1,9,2,4,3,1,8,2,10,9]))

def main():
    solve = Solution()
    n, m = map(int, input().split())
    spisok = list(map(int, input().split()))
    print(solve.solve(n=n, k=m, a=spisok))


if __name__ == "__main__": main()
