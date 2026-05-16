from collections import defaultdict

class Solution:
    from typing import List
    def tupleSameProduct(self, nums: List[int]) -> int:
        productCnt, n, result = defaultdict(int), len(nums), 0
        for i in range(n):
            for j in range(i + 1, n):
                product = nums[i] * nums[j]
                productCnt[product] += 1
        # Считаем кол-во кортежей для каждого произведения
        for count in productCnt.values():
            if count >= 2:
                result += count * (count - 1) * 4
        return result

# Runtime 343 ms, 71 %
# Memory 46.37 mb, 65.40 %
def main():
    solution = Solution()
    print(solution.tupleSameProduct(nums=[2,3,4,6]))
    print(solution.tupleSameProduct(nums=[1,2,4,5,10]))

if __name__ == '__main__':
    main()
