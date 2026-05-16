from collections import defaultdict

class Solution:
    from typing import List
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        colors_to_dict = {}
        result, color_count = [], defaultdict(int)

        for x, y in queries:
            if x in colors_to_dict:
                old_color = colors_to_dict[x]
                color_count[old_color] -= 1
                if color_count[old_color] == 0:
                    del color_count[old_color]

            colors_to_dict[x] = y
            color_count[y] += 1
            result.append(len(color_count))

        return result

# Runtime 69 ms, 70.73 %
# Memory 63.24 mb, 43.56 %
def main():
    solution = Solution()
    limit1, queries1 = 4, [[1,4],[2,5],[1,3],[3,4]]
    limit2, queries2 = 4, [[0,1],[1,2],[2,2],[3,4],[4,5]]
    print(solution.queryResults(limit=limit1, queries=queries1))
    print(solution.queryResults(limit=limit2, queries=queries2))

if __name__ == '__main__':
    main()
