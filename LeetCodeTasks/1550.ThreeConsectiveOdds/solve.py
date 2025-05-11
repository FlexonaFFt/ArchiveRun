class Solution:
    def threeConsecutiveOdds(self, arr: list[int]) -> bool:
        if len(arr) < 3:
            return False

        for i in range(2, len(arr), 1):
            if arr[i - 2] % 2 != 0 and arr[i - 1] % 2 != 0 and arr[i] % 2 != 0:
                return True
            continue

        return False

# Runtime 0 ms, 100 %
# Memory 17.88mb, 61.69 %
def main():
    solution = Solution()
    print(solution.threeConsecutiveOdds(arr=[2,6,4,1]))
    print(solution.threeConsecutiveOdds(arr=[1,2,34,3,4,5,7,23,12]))

if __name__ == '__main__':
    main()
