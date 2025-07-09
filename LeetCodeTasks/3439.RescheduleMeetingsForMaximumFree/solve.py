class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: list[int], endTime: list[int]) -> int: 

        gaps, length = [], len(startTime)
        gaps.append(startTime[0] - 0)
        for i in range(1, length):
            gaps.append(startTime[i] - endTime[i - 1])
        gaps.append(eventTime - endTime[-1])

        # Бален, надо искать теперь сумму через окно
        window = k + 1
        max_sum = current_sum = sum(gaps[:window])
        for i in range(window, len(gaps)):
            current_sum += gaps[i] - gaps[i - window]
            max_sum = max(max_sum, current_sum)

        return max_sum 


def test():
    solve = Solution()
    print(solve.maxFreeTime(5, 1, [1,3], [2,5]))
    print(solve.maxFreeTime(10, 1, [0,2,9], [1,4,10]))
    print(solve.maxFreeTime(5, 2, [0,1,2,3,4], [1,2,3,4,5]))


if __name__ == '__main__':
    test()
