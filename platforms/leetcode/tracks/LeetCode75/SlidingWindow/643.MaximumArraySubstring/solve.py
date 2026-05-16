class Solution:
    from typing import List
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        def sliding_window(array, window):
            for i in range(len(array) - window + 1):
                yield array[i:i + window]

        # Основное тело функции
        max_sum = float("-inf")
        for window in sliding_window(nums, k):
            current_average = sum(window) / len(window)
            if current_average > max_sum:
                max_sum = current_average
        return max_sum

# Мое решение не проходит 122 тест.
# Нехватает времени
def main():
    array, k = [1,12,-5,-6,50,3], 4
    solution = Solution()
    print(solution.findMaxAverage(array, k))

if __name__ == '__main__':
    main()
