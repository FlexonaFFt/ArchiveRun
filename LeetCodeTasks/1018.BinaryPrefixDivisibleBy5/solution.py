class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        result: List[int] = []
        ostatok = 0

        for bit in nums:
            ostatok = (ostatok * 2 + bit) % 5
            result.append(ostatok == 0)
        return result
