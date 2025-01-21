class Solution:
    from typing import List
    def longestOnes(self, numbers: List[int], k: int) -> int:
        left, zero_cnt = 0, 0
        for right in range(len(numbers)):
            if numbers[right] == 0:
                zero_cnt += 1
            while zero_cnt > k:
                if numbers[left] == 0:
                    zero_cnt -= 1
                left += 1
        return len(numbers) - left


def main():
    nums, k = [0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3
    solution = Solution()
    print(solution.longestOnes(nums, k))

if __name__ == '__main__':
    main()
