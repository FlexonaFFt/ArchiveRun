from typing import List

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        minDiff, output = 10*10**5, []
        for i in range(1, len(arr)):
            diff = arr[i] - arr[i - 1]
            if diff < minDiff: minDiff = diff

        for i in range(1, len(arr)):
            if arr[i] - arr[i - 1] == minDiff:
                output.append([arr[i - 1], arr[i]])
        
        return output
