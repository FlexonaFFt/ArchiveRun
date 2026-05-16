class Solution:
    from typing import List
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quickselect(left, right, k_smallest):
            if left == right:
                return nums[left]

            pivot_idx = partition(left, right)
            if k_smallest == pivot_idx:
                return nums[k_smallest]
            elif k_smallest < pivot_idx:
                return quickselect(left, pivot_idx - 1, k_smallest)
            else:
                return quickselect(pivot_idx + 1, right, k_smallest)

        def partition(left, right):
            pivot = nums[right]
            store_idx = left

            for i in range(left, right):
                if nums[i] > pivot:
                    nums[store_idx], nums[i] = nums[i],nums[store_idx]
                    store_idx += 1

            nums[right], nums[store_idx] = nums[store_idx], nums[right]
            return store_idx

        left, right = 0, len(nums) - 1
        return quickselect(0, len(nums) - 1, k - 1)

# Решение не проходит 41 тест из 42 -> (TL)
def main():
    solution = Solution()
    print(solution.findKthLargest(nums=[3,2,1,5,6,4], k=2))
    print(solution.findKthLargest(nums=[3,2,3,1,2,4,5,5,6], k=4))

if __name__ == '__main__':
    main()
