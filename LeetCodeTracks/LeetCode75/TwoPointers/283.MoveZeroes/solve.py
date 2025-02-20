class Solution:
    from typing import List 
    def moveZeroes(self, nums: List[int]) -> List[int]:
        counter, answer = 0, []
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] == 0:
                counter += 1
                left += 1
            elif nums[right] == 0:
                counter += 1
                right -= 1
            else:
                if left <= right:
                    answer.append(nums[left])
                    left += 1
                if left >= right:
                    answer.append(nums[right])
                    right -= 1
        for _ in range(counter):
            answer.append(0)
        return answer


def main():
    solution = Solution()
    input_list = [0,1,0,3,12]
    print(solution.moveZeroes(nums=input_list))

if __name__ == '__main__':
    main()
