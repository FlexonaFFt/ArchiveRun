class Solution:
    def removingDuplicates(self, nums: list[int]) -> int:
        result, counter = [], len(nums)
        for num in nums:
            if num not in result:
                counter -= 1
                result.append(num)
            else: continue
        for _ in range(counter):
            result.append(_)
        return result 


def test():
    solution = Solution()
    print(solution.removingDuplicates([1,1,2]))
    print(solution.removingDuplicates([0,0,1,1,1,2,2,3,3,4]))

test()
