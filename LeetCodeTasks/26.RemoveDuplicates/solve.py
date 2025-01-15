class Solution:
    from typing import List
    def RemoveDuplicates(self, nums: List[int]):
        unique_list, slash_counter = [], 0
        for num in nums:
            if num not in unique_list:
                unique_list.append(num)
            else:
                slash_counter += 1

        # Алгоритм добавления пропусков
        answer_list = ''
        for num in unique_list:
            answer_list += f'{num},'
        for _ in range(1, slash_counter + 1):
            answer_list += '_,'
        answer_list = f'[{answer_list[:-1]}]'
        return slash_counter, answer_list


def main():
    numbers = [0,0,1,1,1,2,2,3,3,4]
    solution = Solution()
    print(solution.RemoveDuplicates(numbers))

if __name__ == '__main__':
    main()
