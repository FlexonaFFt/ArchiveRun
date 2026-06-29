class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        counter, rule, first = 0, True, True 
        for element in nums:
            if element == 1 and first:
                first = False 
            elif element == 0 and first == False:
                counter += 1
            elif element == 1 and first == False:
                if counter < k: 
                    rule = False
                    return rule
                counter = 0
        return rule
