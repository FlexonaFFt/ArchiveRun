class Solution:
    def maximumTripletValue(self, nums: list[int]) -> int:
        res, imax, dmax = 0, 0, 0
        for k in range(len(nums)):
            res = max(res, dmax * nums[k])
            dmax = max(dmax, imax - nums[k])
            imax = max(imax, nums[k])
        return res

'''
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for k in range(2, n):
            maxPrefix = nums[0]
            for j in range(1, k):
                res = max(res, (maxPrefix - nums[j]) * nums[k])
                maxPrefix = max(maxPrefix, nums[j])
        return res
'''

# Runtime 1 ms, 89 %
# Memory 17.94 mb, 19.20 %
def main():
    solution = Solution()
    print(solution.maximumTripletValue(nums=[12,6,1,2,7]))
    print(solution.maximumTripletValue(nums=[1,10,3,4,19]))
    print(solution.maximumTripletValue(nums=[1,2,3]))

main()
