class Solution:
    def divideArray(self, nums: list[int]) -> bool:
        spisok, status = {}, True
        for num in nums:
            if num not in spisok:
                spisok[num] = 1
            else:
                spisok[num] += 1

        for key, value in spisok.items():
            if value % 2 != 0:
                status = False
            continue
        return status

# Runtime 2 ms, 77.39 %
# Memory 17.75 mb, 91.41 %
def main():
    solution = Solution()
    print(solution.divideArray(nums=[3,2,3,2,2,2]))
    print(solution.divideArray(nums=[1,2,3,4]))

if __name__ == '__main__':
    main()
