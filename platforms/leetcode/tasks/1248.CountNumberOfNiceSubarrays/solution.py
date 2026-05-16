class Solution:
    from typing import List
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        curr_sum, sub_arr = 0, 0
        prefix_sum = {curr_sum: 1}
        for i in range(len(nums)):
            curr_sum += nums[i] % 2
            if curr_sum - k in prefix_sum:
                sub_arr = sub_arr + prefix_sum[curr_sum - k]
            prefix_sum[curr_sum] = prefix_sum.get(curr_sum, 0) + 1
        return sub_arr


def main():
    solution = Solution()
    print(solution.numberOfSubarrays([1,1,2,1,1], 3))
    print(solution.numberOfSubarrays([2,4,6], 1))
    print(solution.numberOfSubarrays([2,2,2,1,2,2,1,2,2,2], 2))

if __name__ == '__main__':
    main()
