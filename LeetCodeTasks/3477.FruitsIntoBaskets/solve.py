class Solution:
    def numOfUnplacedFruits(self, fruits: list[int], baskets: list[int]) -> int:
        counter, n = 0, len(baskets)
        for fruit in fruits:
            unset = 1
            for i in range(n):
                if fruit <= baskets[i]:
                    baskets[i], unset = 0, 0
                    break 
            counter += unset

        return counter 


# Runtime 19 ms, 69.23 %
# Memory 17.78 mb, 83.86 %
def test():
    solve = Solution()
    print(solve.numOfUnplacedFruits([4,2,5], [3,5,4]))
    print(solve.numOfUnplacedFruits([3,6,1], [6,4,7]))

if __name__ == '__main__':
    test()
