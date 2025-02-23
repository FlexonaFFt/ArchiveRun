import heapq
class Solution:
    from typing import List
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]

# Runtime 103 ms, 24.28 %
# Memory 28.74 mb, 46.75 %
def main():
    solution = Solution()
    print(solution.findKthLargest(nums=[3,2,1,5,6,4], k=2))
    print(solution.findKthLargest(nums=[3,2,3,1,2,4,5,5,6], k=4))

if __name__ == '__main__':
    main()
