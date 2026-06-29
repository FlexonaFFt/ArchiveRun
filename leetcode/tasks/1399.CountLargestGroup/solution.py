class Solution:
    def countLargestGroup(self, n: int) -> int:
        def digit_sum(n: int) -> int:
            s = 0
            while n > 0:
                s += n % 10 
                n //= 10
            return s 
        
        g = {}
        for k in range(1, n + 1):
            a = digit_sum(k)
            if a not in g:
                g[a] = 1
            else: g[a] += 1
        
        m = max(g.values())
        return sum(1 for v in g.values() if v == m)


def test():
    solve = Solution()
    print(solve.countLargestGroup(13))
    print(solve.countLargestGroup(2))

if __name__ == '__main__':
    test()
