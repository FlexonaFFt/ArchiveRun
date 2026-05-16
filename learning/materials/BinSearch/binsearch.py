class BinSearch:
    from typing import List
    def search(self, arr: List[int], value: int) -> bool:
        if not arr:
            return False

        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == value:
                return True
            elif arr[mid] > value:
                right = mid - 1
            else:
                left = mid + 1
        return False


def main():
    solve = BinSearch()
    print(solve.search([3,4,5,6,7,8,9], 7))

if __name__ == '__main__':
    main()
