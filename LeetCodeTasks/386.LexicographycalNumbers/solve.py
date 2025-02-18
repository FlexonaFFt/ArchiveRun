class Solution:
    from typing import List
    def lexicalOrder(self, n: int) -> List[int]:
        unsortedList = []
        for i in range(1, n + 1):
            unsortedList.append(i)
        for element in unsortedList:
            if ord(element)


def main():
    solve = Solution()
    print(solve.lexicalOrder(n=13))
    print(solve.lexicalOrder(n=2))

if __name__ == '__main__':
    main()
