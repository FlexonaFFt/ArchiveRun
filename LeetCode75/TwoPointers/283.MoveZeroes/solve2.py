class Solution:
    from typing import List 
    def moveZeroes(self, nums: List[int]) -> List[int]:
        flag, cool = 0, len(nums)
        for current in range(cool):
            if nums[current] != 0:
                nums[flag], nums[current] = nums[current], nums[flag]
                flag += 1
        return nums 
        
# Runtime 3 ms, 82.37 %
# Memory 19.01 mb, 5.36 %
def main():
    solution = Solution()
    input_list = [0,1,0,3,12]
    print(solution.moveZeroes(nums=input_list))

if __name__ == '__main__':
    main()
