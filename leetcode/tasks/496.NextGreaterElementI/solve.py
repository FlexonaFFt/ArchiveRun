class Solution:
    from typing import List
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack, next_greather = [], {}
        for num in nums2:
            while stack and stack[-1] < num:
                next_greather[stack.pop()] = num
            stack.append(num)

        while stack:
            next_greather[stack.pop()] = -1
        answerList = [next_greather.get(num, -1) for num in nums1]
        return answerList

# Runtime 0 ms, 100 %
# Memory 17.94 mb, 53.93 %
def main():
    solve = Solution()
    test1, test2 = [4,1,2], [1,3,4,2]
    test3, test4 = [2, 4], [1,2,3,4]
    print(solve.nextGreaterElement(test1, test2))
    print(solve.nextGreaterElement(test3, test4))

if __name__ == '__main__':
    main()
