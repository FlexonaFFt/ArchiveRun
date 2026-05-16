class Solution:
    from typing import List
    def SelectionSort(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            min_index = i
            for j in range(i + 1, len(nums)):
                if nums[j] < nums[min_index]:
                    min_index = j
            nums[i], nums[min_index] = nums[min_index], nums[i]
        return nums

def main():
    solve = Solution()
    n = int(input())
    array = list(map(int, input().split()))
    print(*solve.SelectionSort(array))

if __name__ == '__main__':
    main()
