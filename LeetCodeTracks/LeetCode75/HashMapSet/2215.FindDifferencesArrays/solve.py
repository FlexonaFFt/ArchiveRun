class Solution:
    from typing import List
    def findDifference(self, nums1: List[int],
        nums2: List[int]) -> List[List[int]]:
        first, second = [], []
        for element in nums1:
            if element not in nums2 and element not in first:
                first.append(element)
        for element in nums2:
            if element not in nums1 and element not in second:
                second.append(element)
        answer = [first, second]
        return answer

# Runtime 455 ms, 6.36 %
# Memory 18.07 mb, 42.94 %
def main():
    nums1, nums2 = [1,2,3], [2,4,6]
    nums3, nums4 = [1,2,3,3], [1,1,2,2]
    solution = Solution()
    print(solution.findDifference(nums1, nums2))
    print(solution.findDifference(nums3, nums4))

if __name__ == '__main__':
    main()
