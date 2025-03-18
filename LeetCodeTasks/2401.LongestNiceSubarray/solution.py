class Solution:
    def longestNiceSubarray(self, nums: list[int]) -> int:
        n, max_length = len(nums), 1
        left, used_bits = 0, 0

        for right in range(n):
            # Проверяем есть ли общие биты с used_bits - уже использованными битами
            while used_bits & nums[right] != 0:
                # Удаляет биты элемента nums[left] из used_bits
                used_bits ^= nums[left]
                left += 1
            # Добавляем биты текущего элемента
            used_bits |= nums[right]
            max_length = max(max_length, right - left + 1)

        return max_length

# Runtime 95 ms, 47 %
# Memory 31.94 mb, 57 %
def main():
    solve = Solution()
    print(solve.longestNiceSubarray(nums=[1,3,8,48,10]))
    print(solve.longestNiceSubarray(nums=[3,1,5,11,13]))

main()
