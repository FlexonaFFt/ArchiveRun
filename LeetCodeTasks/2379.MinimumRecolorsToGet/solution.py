class Solution:
    def minimumRecolors(self, blocks: str, k: int):
        left, num_whites, num_recolors = 0, 0, float('inf')
        for right in range(len(blocks)):
            if blocks[right] == 'W':
                num_whites += 1
            if right - left + 1 == k:
                num_recolors = min(num_recolors, num_whites)
                if blocks[left] == 'W':
                    num_whites -= 1
                left += 1
        return num_recolors

# Runtime 4 ms, 15.26 %
# Memory 17.62 mb, 88.78 %
def main():
    solution = Solution()
    print(solution.minimumRecolors(blocks="WBBWWBBWBW", k=7))
    print(solution.minimumRecolors(blocks="WBWBBBW", k=2))

if __name__ == '__main__':
    main()
