'''class Solution:
    from typing import List
    def plusOne(self, digits: List[int]) -> List[int]: 
        if digits[-1] + 1 < 10:
            digits[-1] + 1
            return digits 
        else:
            digits[-1] = 0
            digits[-2] + 1
            return digits'''

class Solution:
    from typing import List
    def plusOne(self, digits: List[int]) -> List[int]: 
        n = len(digits)
        for i in range(n - 1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        return [1] + digits 

# Runtime 0 ms
# Memory 17.92 mb, Beats 14.73 %
def main():
    numbers = list(map(int, input().split()))
    solution = Solution()
    print(solution.plusOne(digits=numbers))

if __name__ == '__main__':
    main()
