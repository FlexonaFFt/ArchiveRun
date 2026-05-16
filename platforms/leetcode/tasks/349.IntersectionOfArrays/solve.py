class Solution:
    from typing import List
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answer = []
        for element in nums1:
            if element in nums2 and element not in answer:
                answer.append(element)
        return answer

# Runtime 11 ms, 13.79 %
# Memory 17.76 mb, 92.80 %
def main():
    solve = Solution()
    print(solve.intersection(nums1=[1,2,2,1], nums2=[2,2]))
    print(solve.intersection(nums1=[4,9,5], nums2=[9,4,9,8,4]))

if __name__ == '__main__':
    main()
