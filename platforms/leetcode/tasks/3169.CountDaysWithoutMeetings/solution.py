class Solution:
    def countDays(self, days: int, meetings: list[list[int]]):
        counter, counterlist = 0, []
        for timelimit in meetings:
            for i in range(timelimit[0], timelimit[1] + 1):
                if i not in counterlist:
                    counterlist.append(i)
                else:
                    continue

        for j in range(1, days + 1):
            if j not in counterlist:
                counter += 1
            else:
                continue

        return counter

# time limit
def main():
    solve = Solution()
    print(solve.countDays(days=10, meetings=[[5,7],[1,3],[9,10]]))
    print(solve.countDays(days=5, meetings=[[2,4],[1,3]]))
    print(solve.countDays(days=6, meetings=[[1,6]]))

if __name__ == '__main__':
    main()
