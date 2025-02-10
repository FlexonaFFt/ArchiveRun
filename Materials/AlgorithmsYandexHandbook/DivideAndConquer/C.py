class Solution():
    from typing import List
    def Merge(self, left: List[int], right: List[int]) -> List[int]:
        sortedArr = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                sortedArr.append(left[i])
                i += 1
            else:
                sortedArr.append(right[j])
                j += 1
        sortedArr.extend(left[i:])
        sortedArr.extend(right[j:])
        return sortedArr

    def MergeSort(self, arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left_half = self.MergeSort(arr[:mid])
        right_half = self.MergeSort(arr[mid:])
        return self.Merge(left_half, right_half)


def main():
    solution = Solution()
    n = int(input())
    array = list(map(int, input().split()))
    sorted_arr = solution.MergeSort(array)
    print(' '.join(map(str, sorted_arr)))

if __name__ == '__main__':
    main()
