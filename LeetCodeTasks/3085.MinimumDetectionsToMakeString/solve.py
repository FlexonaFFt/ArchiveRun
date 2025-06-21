from collections import defaultdict
class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        counter, res = defaultdict(int), len(word)
        for c in word: counter[c] += 1
        for a in counter.values():
            deleted = 0
            for b in counter.values():
                if a > b: deleted += b
                elif b > a + k: deleted += b - (a + k)
            res = min(res, deleted)
        return res

# Runtime 87 ms, 33.33 %
# Meomry 18.14 mb, 45.74 %
def test():
    solve = Solution()
    print(solve.minimumDeletions("aabcaba", 0))
    print(solve.minimumDeletions("dabdcbdcdcd", 2))
    print(solve.minimumDeletions("aaabaaa", 2))

if __name__ == '__main__':
    test()
