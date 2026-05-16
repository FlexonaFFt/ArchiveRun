class Solution:
    from typing import List
    def lexicographicallySmallestArray(self, nums: List[int],
        limit: int) -> List[int]:
        n = len(nums)
        # Сортируем массив с сохранением индексов
        nums_with_idx = [(nums[i], i) for i in range(n)]
        nums_with_idx.sort()
        result, i = [0] * n, 0
        while i < n:
            # Будем находить группу элементов, которая может быть обменяна
            group = []
            group.append(nums_with_idx[i])
            j = i + 1
            while j < n and nums_with_idx[j][0] - nums_with_idx[j - 1][0] <= limit:
                group.append(nums_with_idx[j])
                j += 1
            group.sort(key=lambda x: x[1])
            for k in range(len(group)):
                result[group[k][1]] = nums_with_idx[i + k][0]
            i = j
        return result

# Runtime 291 ms, 81.25 %
# Memory 44.20 mb, 93.75 %
def main():
    solve = Solution()
    nums1, limit1 = [1,5,3,9,8], 2
    nums2, limit2 = [1,7,6,18,2,1], 3
    nums3, limit3 = [1,7,28,19,10], 3
    print(solve.lexicographicallySmallestArray(nums1, limit1))
    print(solve.lexicographicallySmallestArray(nums2, limit2))
    print(solve.lexicographicallySmallestArray(nums3, limit3))

if __name__ == '__main__':
    main()
