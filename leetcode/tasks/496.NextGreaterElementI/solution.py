class Solution:
    from typing import List
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answerList = []
        for element in nums1:
            index = nums2.index(element)
            if nums2[index] != nums2[-1]:
                if nums2[index] > nums2[index + 1]:
                    answerList.append(nums2[index])
                else:
                    answerList.append(-1)
            else:
                answerList.append(nums2[index])
        return answerList

# Решение не проходит тесты
def main():
    solve = Solution()
    test1, test2 = [4,1,2], [1,3,4,2]
    test3, test4 = [2, 4], [1,2,3,4]
    print(solve.nextGreaterElement(test1, test2))
    print(solve.nextGreaterElement(test3, test4))

if __name__ == '__main__':
    main()
