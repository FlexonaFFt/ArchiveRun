class Solution:
    def ver_finder(self, n: int):
        from collections import defaultdict
        dp = [defaultdict(int) for _ in range(n + 1)]
        dp[1][(0, 0, 0)] = 1
        dp[1][(1, 0, 0)] = 1

        for pos in range(1, n):
            for (prev, x, y), count in dp[pos].items():
                if prev == 0: dp[pos + 1][(0, x, y + 1)] += count 
                else: dp[pos + 1][(0, x, y)] += count 

                if prev == 0: dp[pos + 1][(1, x + 1, y)] += count 
                else: dp[pos + 1][(1, x, y)] += count 


        winA = winB = draw = 0
        for (prev, x, y), count in dp[n].items():
            if x > y: winA += count 
            elif x == y: draw += count 
            else: winB += count 

        def pretty(x):
            s = f"{x:.10f}"
            s = s.rstrip('0').rstrip('.')
            if s == '':
                return '0'
            return s

        total = 2 ** n 
        print(f"{pretty(winA/total)} {pretty(draw/total)} {pretty(winB/total)}")


def test():
    solve = Solution()
    solve.ver_finder(1)
    solve.ver_finder(2)
    solve.ver_finder(3)
    solve.ver_finder(4)
    solve.ver_finder(5)

def main():
    n = int(input())
    solve = Solution()
    solve.ver_finder(n)

if __name__ == '__main__': 
    main()
