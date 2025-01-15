# Runtime 0 ms, Beats 100 %
class Solution:
    from typing import List
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0  # Индекс для записи элементов, не равных val
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k

def main():
    numbers, val = [0,1,2,2,3,0,4,2], 2
    solution = Solution()
    k = solution.removeElement(numbers, val)
    print(f'k = {k}, nums = {numbers[:k]}')

if __name__ == '__main__':
    main()
