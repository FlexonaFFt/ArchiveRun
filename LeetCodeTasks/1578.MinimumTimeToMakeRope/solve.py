class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        times, last_keep = 0, 0

        for i in range(1, len(colors)):
            if colors[i] == colors[last_keep]:
                if neededTime[i] < neededTime[last_keep]:
                    times += neededTime[i]
                else:
                    times += neededTime[last_keep]
                    last_keep = i
            else: last_keep = i
        return times
