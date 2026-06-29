class Solution:
    def check(self, nums: List[int]) -> bool:
        
        for rotation in range(len(nums)):
            check = []

            for index in range(rotation, len(nums)):
                check.append(nums[index])
            for index in range(rotation):
                check.append(nums[index])

            sorted = True 
            for index in range(len(nums) - 1):
                if check[index] > check[index + 1]:
                    sorted = False 
                    break 

            if sorted == True: return True 
        return False 
