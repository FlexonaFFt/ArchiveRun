class Solution:
    from typing import List
    def majorityElement(self, nums: List[int]) -> int:
        counter = {}
        for element in nums:
            if element not in counter:
                counter[element] = 1
            else:
                counter[element] += 1
        for key, val in counter.items():
            if val > len(nums) // 2:
                return key

# Runtime 12 ms, 22.29 %
# Memory 19.32 mb, 52.25 %
def main():
    solution = Solution()
    print(solution.majorityElement(nums=[3,2,3]))
    print(solution.majorityElement(nums=[2,2,1,1,1,2,2]))

if __name__ == '__main__':
    main()
