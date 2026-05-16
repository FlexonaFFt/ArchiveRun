class Solution:
    def countDays(self, days: int, meetings: list[list[int]]):
        free_days, latest_end = 0, 0
        meetings.sort()
        for start, end in meetings:
            if start > latest_end + 1:
                free_days += start - latest_end - 1

            latest_end = max(latest_end, end)
        free_days += days - latest_end
        return free_days

# Runtime 222 ms, 25.44 %
# Memory 52.84 mb, 55.42 %
def main():
    solve = Solution()
    print(solve.countDays(days=10, meetings=[[5,7],[1,3],[9,10]]))
    print(solve.countDays(days=5, meetings=[[2,4],[1,3]]))
    print(solve.countDays(days=6, meetings=[[1,6]]))

if __name__ == '__main__':
    main()
