class Solution:
    from typing import List
    def Merge(self, lists: List[List[int]]) -> List[int]:
        result, currentElements = [], []
        iterators = [iter(lst) for lst in lists]
        for it in iterators:
            try:
                currentElements.append(next(it))
            except StopIteration:
                currentElements.append(None)

        while any(elem is not None for elem in currentElements):
            min_val, min_index = float('inf'), -1
            for i, elem in enumerate(currentElements):
                if elem is not None and elem < min_val:
                    min_val = elem
                    min_index = i
            result.append(min_val)
            try:
                currentElements[min_index] = next(iterators[min_index])
            except StopIteration:
                currentElements[min_index] = None
        return result


def main():
    solve = Solution()
    n = int(input())
    lists = []
    for _ in range(n):
        m = int(input())
        lst = list(map(int, input().split()))
        lists.append(lst)
    print(*solve.Merge(lists=lists))

if __name__ == '__main__':
    main()
