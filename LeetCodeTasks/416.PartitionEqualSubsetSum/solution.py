class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2
        possible_sums = set([0])

        for num in nums:
            next_sums = set()
            for s in possible_sums:
                if s + num == target:
                    return True
                next_sums.add(s + num)
                next_sums.add(s)
            possible_sums = next_sums

        return target in possible_sums

def main():
    solution = Solution()
    print(solution.canPartition([1,5,11,5]))
    print(solution.canPartition([1,2,3,5]))

main()
