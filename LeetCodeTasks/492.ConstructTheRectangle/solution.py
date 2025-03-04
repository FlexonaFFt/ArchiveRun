class Solution:
    from typing import List
    def constructRectangle(self, area: int) -> List[int]:
        for l in range(int(area**0.5), 0, -1):
            if area % l == 0:
                return [area // l, l]

# Runtime 0 ms, 100 %
# Memory 17.87 mb, 41 %
def main():
    solution = Solution()
    print(solution.constructRectangle(area=4))
    print(solution.constructRectangle(area=37))
    print(solution.constructRectangle(area=122122))

if __name__ == '__main__':
    main()
