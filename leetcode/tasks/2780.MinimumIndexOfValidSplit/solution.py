from collections import defaultdict
class Solution:
    def minimumIndex(self, nums: list[int]) -> int:
        first, second =  defaultdict(int), defaultdict(int)
        for num in nums: second[num] += 1
        for index in range(len(nums)):
            num = nums[index]
            second[num] -= 1
            first[num] += 1

            if (
                first[num] * 2 > index + 1
                and second[num] * 2 > len(nums) - index - 1
            ):
                return index
        return -1

# Runtime 108 ms, 33.17 %
# Memory 34.76 mb, 13.86 %
def test():
    solution = Solution()
    value1 = solution.minimumIndex(nums=[1,2,2,2])
    value2 = solution.minimumIndex(nums=[2,1,3,1,1,1,7,1,2,1])
    value3 = solution.minimumIndex(nums=[3,3,3,3,7,2,2])

    answer1, answer2, answer3 = 2, 4, -1
    if value1 == answer1 and value2 == answer2 and value3 == answer3:
        print("OK")
        print(value1)
        print(value2)
        print(value3)
    else: print("WA")

test()
