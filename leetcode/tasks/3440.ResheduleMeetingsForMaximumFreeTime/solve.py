class Solution:
    def maxFreeTime(self, eventTime: int, startTime: list[int], endTime: list[int]) -> int: 
        n, max_free = len(startTime), 0
        meetings = sorted(zip(startTime, endTime))

        def calc_max_gap(meetings):
            prev, max_gap = 0, 0
            for s, e in meetings:
                max_gap = max(max_gap, s - prev)
                prev = e

            max_gap = max(max_gap, eventTime - prev)
            return max_gap

        max_free = calc_max_gap(meetings)
        for i in range(n):
            new_meetings = meetings[i:] + meetings[i+1:]
            duration = meetings[i][1] - meetings[i][0]
            prev_end = 0

            for j in range(len(new_meetings) + 1):
                if j == len(new_meetings):
                    gap_start = prev_end
                    gap_end = eventTime
                else:
                    gap_start = prev_end
                    gap_end = new_meetings[j][0]

                if gap_end - gap_start >= duration:
                    inserted = new_meetings[j:] + [(gap_start, gap_start + duration)] + new_meetings[j:]
                    inserted.sort()
                    max_gap = calc_max_gap(inserted)
                    max_free = max(max_free, max_gap)
                prev_end = new_meetings[j][1] if j < len(new_meetings) else prev_end

        return max_free 



def test():
    solve = Solution()
    print(solve.maxFreeTime(5, [1,3], [2,5]))
    print(solve.maxFreeTime(10, [0,7,9], [1,8,10]))
    print(solve.maxFreeTime(5, [0,3,7,9], [1,4,8,10]))
    print(solve.maxFreeTime(5, [0,1,2,3,4], [1,2,3,4,5]))


if __name__ == '__main__':
    test()
