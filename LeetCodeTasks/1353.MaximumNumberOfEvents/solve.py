import heapq

class Solution:
    def maxEvents(self, events: list[list[int]]) -> int:

        events.sort()
        total_events, min_heap = len(events), []
        event_id, attended = 0, 0
        last_day = max(end for _, end in events)

        for day in range(1, last_day + 1):
            while event_id < total_events and events[event_id][0] == day:
                heapq.heappush(min_heap, events[event_id][1])
                event_id += 1

            while min_heap and min_heap[0] < day:
                heapq.heappop(min_heap)

            if min_heap:
                heapq.heappop(min_heap)
                attended += 1

        return attended

# Runtime 162 ms, 38.92 %
# Memory 53.25 mb, 55.87 %
def test():
    solve = Solution()
    print(solve.maxEvents(events=[[1,2],[2,3],[3,4]]))
    print(solve.maxEvents(events=[[1,2],[2,3],[3,4],[1,2]]))


if __name__ == '__main__': 
    test()
