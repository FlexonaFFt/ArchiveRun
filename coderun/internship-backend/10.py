class Solution:

    def main(self, n: int, nums: list[int]) -> int:
        # задаем границы для работы алгоритма
        nums = [0] + nums
        nums += [0]

        out, lefts = 0, [0]
        for curr in range(1, n + 2):

            while nums[curr] < nums[lefts[-1]]:
                area = nums[lefts.pop()] * (curr - lefts[-1] - 1)
                if area > out: out = area 

            # Если текущая высота меньше или равна вершине стека
            if nums[curr] <= nums[lefts[-1]]: lefts[-1] = curr 
            else: lefts.append(curr)
        return out

    def inputer(self) -> None:
        string = list(map(int, input().split()))
        s, string_of_nums = string[0], string[1:]
        print(self.main(s, string_of_nums))


if __name__ == '__main__': Solution().inputer()