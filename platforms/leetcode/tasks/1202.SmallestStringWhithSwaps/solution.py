from collections import defaultdict


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: list[list[int]]):
        p = list(range(len(s)))

        def find(x):
            if x != p[x]:
                p[x] = find(p[x])
            return p[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                p[py] = px

        for x, y in pairs:
            union(x, y)

        dict = defaultdict(list)
        for idx_list = dic[key]


def main():
    solution = Solution()
    print(solution.smallestStringWithSwaps(s='abcb', pairs=[]))

main()
