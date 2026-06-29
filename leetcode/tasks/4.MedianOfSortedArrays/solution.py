class Solution:
    from typing import List
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        low, high = 0, m

        while low <= high:
            partition1 = (low + high) // 2
            partition2 = (m + n + 1) // 2 - partition1

            max_left1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
            min_right1 = float('inf') if partition1 == m else nums1[partition1]
            max_left2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
            min_right2 = float('inf') if partition2 == n else nums2[partition2]

            if max_left1 <= min_right2 and max_left2 <= min_right1:
                if (m + n) % 2 == 0:
                    return (max(max_left1, max_left2) + min(min_right1, min_right2)) / 2
                else:
                    return max(max_left1, max_left2)
            elif max_left1 > max_left2:
                high = partition1 - 1
            else:
                low = partition1 + 1

        raise ValueError("Input arrays are not sorted or invalid input")

# Runtime 2 ms, 59.5 %
# Memory 18.34 mb, 6.23 %
def main():
    solution = Solution()
    print(solution.findMedianSortedArrays(nums1=[1, 2], nums2=[2]))
    print(solution.findMedianSortedArrays(nums1=[1, 2], nums2=[3, 4]))

if __name__ == '__main__':
    main()
