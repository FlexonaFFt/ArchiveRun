class Solution:
    def countDays(self, days: int, meetings: list[list[int]]):
        counter, busy_days = 0 ,set()
        for start, end in meetings:
            busy_days.update(range(start, end + 1))
        return days - len(busy_days)

# memory limit
def main():
    solve = Solution()
    print(solve.countDays(days=10, meetings=[[5,7],[1,3],[9,10]]))
    print(solve.countDays(days=5, meetings=[[2,4],[1,3]]))
    print(solve.countDays(days=6, meetings=[[1,6]]))

if __name__ == '__main__':
    main()
