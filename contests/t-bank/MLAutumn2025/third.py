from collections import Counter

MOD = 10**9 + 7

class Solution:
    def func(self, n: int, arr: list) -> int:
        freq = Counter(arr)
        ans = 1
        for c in freq.values():
            ans = (ans * (c + 1)) % MOD
        ans = (ans - 1) % MOD
        return ans

def main():
    n = int(input().strip())
    array = list(map(int, input().split()))
    print(Solution().func(n, array))

if __name__ == '__main__':
    main()
