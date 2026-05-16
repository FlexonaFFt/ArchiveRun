class Solution:
    from typing import List
    def greedyMeetingRoom(self, n: int, times: List[int]) -> int:
        times.sort(key=lambda x: x[1])
        count, lastEnd = 0, -1

        for start, end in times:
            if start > lastEnd:
                count += 1
                lastEnd = end
        return count


def main():
    solution = Solution()
    n = int(input())
    times = []
    for _ in range(n):
        n, k = map(int, input().split())
        times.append((n, k))
    print(solution.greedyMeetingRoom(n, times))

if __name__ == '__main__':
    main()
