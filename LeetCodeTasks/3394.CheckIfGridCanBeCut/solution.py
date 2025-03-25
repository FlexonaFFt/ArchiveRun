class Solution:
    def checkValidCuts(self, n: int, rectangles: list[list[int]]) -> bool:

        def canSplit(intervals: list[list[int]]) -> bool:
            intervals.sort()
            cuts, current_end = 0, intervals[0][1]

            for start, end in intervals:
                if start >= current_end:
                    cuts += 1
                    if cuts >= 2:
                        return True
                current_end = max(current_end, end)
            return False

        x_intervals = [[x1, x2] for x1, _, x2, _ in rectangles]
        y_intervals = [[y1, y2] for _, y1, _, y2 in rectangles]

        return canSplit(x_intervals) or canSplit(y_intervals)

# Runtime 527 ms, 41.22 %
# Memory 83.58 mb, 70.72 %
def test():
    solution = Solution()
    val1 = solution.checkValidCuts(5, [[1,0,5,2],[0,2,2,4],[3,2,5,3],[0,4,4,5]])
    val2 = solution.checkValidCuts(4, [[0,0,1,1],[2,0,3,4],[0,2,2,3],[3,0,4,3]])
    val3 = solution.checkValidCuts(4, [[0,2,2,4],[1,0,3,2],[2,2,3,4],[3,0,4,2],[3,2,4,4]])

    ans1 = True
    ans2 = False
    ans3 = False

    print(f"{val1 == ans1}, Ответ: {val1}")
    print(f"{val2 == val2}, Ответ: {val2}")
    print(f"{val3 == ans3}, Ответ: {val3}")

if __name__ == '__main__':
    test()
