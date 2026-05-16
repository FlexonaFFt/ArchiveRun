class Solution:
    from typing import List
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0

        items_pointer, valid_items = 0, []
        for i in range(len(nums)):
            if nums[i] != val:
                valid_items.append(nums[i])
                items_pointer += 1

        # Алгоритм добавления пропусков
        answer_list = ''
        for num in valid_items:
            answer_list += f'{num},'
        for _ in range(len(nums) - items_pointer):
            answer_list += '_,'
        answer_list = f'[{answer_list[:-1]}]'       
        print(f'{items_pointer}, nums = {answer_list}')


def main():
    numbers, val = [0,1,2,2,3,0,4,2], 2
    solution = Solution()
    solution.removeElement(numbers, val)

if __name__ == '__main__':
    main()

'''solution = Solution()
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
k = solution.removeDuplicates(nums)
print(f"k = {k}, nums = {nums[:k] + ['_'] * (len(nums) - k)}")'''
