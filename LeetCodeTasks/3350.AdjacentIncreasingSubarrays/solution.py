class Solution:
    def maxIncreasingSubarrays(self, nums: list[int]) -> int:
        answer, predcounter, counter = 0, 0, 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                counter += 1
            else:
                predcounter, counter = counter, 1

            answer = max(answer, min(predcounter, counter))
            answer = max(answer, counter // 2)
        return answer 


def test():
    solve = Solution()
    print(solve.maxIncreasingSubarrays(nums=[2,5,7,8,9,2,3,4,3,1]))
    print(solve.maxIncreasingSubarrays(nums=[1,2,3,4,4,4,4,5,6,7]))

if __name__ == '__main__':
    test()
