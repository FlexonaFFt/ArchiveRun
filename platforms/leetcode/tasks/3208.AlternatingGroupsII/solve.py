class Solution:
    from typing import List
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n, count, left = len(colors), 0, 0
        for right in range(n + k - 1):
            # Проверка на чередование
            if right > 0 and colors[right % n] == colors[(right - 1) % n]:
                left = right
            if right - left + 1 >= k:
                count += 1
        return count

# Runtime 771 ms, 24.25 %
# Memory 21.24 mb, 72.76 %
def main():
    solve = Solution()
    print(solve.numberOfAlternatingGroups([0,1,0,1,0], 3))
    print(solve.numberOfAlternatingGroups([0,1,0,0,1,0,1], 6))
    print(solve.numberOfAlternatingGroups([1,1,0,1], 4))

if __name__ == '__main__':
    main()
