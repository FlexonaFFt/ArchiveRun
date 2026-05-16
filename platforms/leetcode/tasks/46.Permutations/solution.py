from itertools import permutations
class Solution:
    from typing import List
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer, perms = [], permutations(nums)
        for perm in perms:
            iter = []
            for item in perm:
                iter.append(item)
            answer.append(iter)
        return answer

# Runtime 0 ms, 100 %
# Memory 17.96 mb, 52.25 %
def main():
    solution = Solution()
    print(solution.permute(nums=[1,2,3]))
    print(solution.permute(nums=[0,1]))
    print(solution.permute(nums=[1]))

if __name__ == '__main__':
    main()
