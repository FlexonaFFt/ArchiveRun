import heapq
class Solution:
    from typing import List
    def minOperations(self, nums: List[int], k: int) -> int:
        counter = 0
        heapq.heapify(nums)
        while nums[0] < k and len(nums) >= 2:
            smallest, secSmallest = heapq.heappop(nums), heapq.heappop(nums)
            number = ((min(smallest, secSmallest) * 2 + max(smallest, secSmallest)))
            heapq.heappush(nums, number)
            counter += 1
        if nums and nums[0] < k:
            return -1
        return counter

# Runtime 257 ms, 44.12 %
# Memory 35.51 mb, 38.24 %
def main():
    solution = Solution()
    print(solution.minOperations(nums=[2,11,10,1,3], k=10))
    print(solution.minOperations(nums=[1,1,2,4,9], k=20))

if __name__ == '__main__':
    main()
