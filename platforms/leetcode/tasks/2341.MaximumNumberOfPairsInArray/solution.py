class Solution:
    def numberOfPairs(self, nums: list[int]) -> list[int]:
        slovar = {}
        for num in nums:
            if num in slovar:
                slovar[num] += 1
            else:
                slovar[num] = 1

        pairs, leftover = 0, 0
        for value in slovar.values():
            pairs += value // 2
            leftover += value % 2

        return [pairs, leftover]

# Runtime 0 ms, 100 %
# Memory 18.02 mb, 21.19 %
def main():
    solve = Solution()
    print(solve.numberOfPairs(nums=[1, 3, 2, 1, 3, 2, 2]))
    print(solve.numberOfPairs(nums=[1, 1]))
    print(solve.numberOfPairs(nums=[0]))

main()
