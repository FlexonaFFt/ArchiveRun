class Solution:
    from typing import List 
    def canPlaceFlowers(self, sections: List[int], flowers: int) -> bool:
        sections = [0] + sections + [0]
        counter = 0
        for i in range(1, len(sections) - 1):
            if sections[i] == 0 and sections[i - 1] == 0 and sections[i + 1] == 0:
                counter += 1
                sections[i] = 1
        return counter >= flowers 

# Runtime 12 ms, 23.82 %
# Memory 18.36 mb, 7.53 % 
def main():
    flowered = [1, 0, 0, 0, 1]
    flowers = 1
    solution = Solution()
    print(solution.canPlaceFlowers(flowered, flowers))

if __name__ == '__main__':
    main()
