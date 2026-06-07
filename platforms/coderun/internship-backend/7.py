class Solution:

    def main(self, n):
        if n == 1: return 2
        d0, d1, d11 = 1, 1, 0
        for _ in range(n - 1):
            d0, d1, d11 = d0 + d1 + d11, d0, d1 
        
        return d0 + d1 + d11

    def func(self) -> None:
        n = int(input())
        print(self.main(n=n))


if __name__ == '__main__':
    Solution().func()