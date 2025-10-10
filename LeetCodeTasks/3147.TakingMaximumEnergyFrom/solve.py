class Solution:
    def maximumEnergy(self, energy: list[int], k: int) -> int:
        maxSum= -10**8

        for i in range(len(energy)):
            summa, j = 0, i 
            while j < len(energy):
                summa += energy[j]
                j += k 
            if summa > maxSum:
                maxSum = summa 
        return maxSum


def test():
    solve = Solution()
    print(solve.maximumEnergy([5,2,-10,-5,1], 3))
    print(solve.maximumEnergy([-2,-3,-1], 2))

if __name__ == '__main__':
    test()
