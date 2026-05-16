class Solution:
    def clearStars(self, s: str) -> str:
        cnt, arr = [[] for _ in range(26)], list(s)
        for i, c in enumerate(arr):
            if c != "*": cnt[ord(c) - ord("a")].append(i)
            else:
                for j in range(26):
                    if cnt[j]:
                        arr[cnt[j].pop()] = '*'
                        break
        return ''.join(c for c in arr if c != '*')


# Runtime 496 ms, 77.70 %
# Memory 23.47 mb, 73.38 %
def test():
    solve = Solution()
    print(solve.clearStars(s="aaba*"))
    print(solve.clearStars(s="abc"))

if __name__ == '__main__': test()
