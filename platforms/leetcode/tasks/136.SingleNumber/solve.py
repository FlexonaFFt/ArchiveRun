class Solution:
    from typing import List
    def singleNumber(self, nums: List[int]) -> int:
        counter = {}
        for element in nums:
            if element not in counter:
                counter[element] = 1
            else:
                counter[element] += 1
        generator = [key for key, value in counter.items() if value == 1]
        return generator[0]

# Runtime 11 ms, 19.09 %
# Memory 19.83 mb, 14.64 %
def main():
    solution = Solution()
    print(solution.singleNumber(nums=[2,2,1]))
    print(solution.singleNumber(nums=[4,1,2,1,2]))
    print(solution.singleNumber(nums=[1]))

if __name__ == '__main__':
    main()
