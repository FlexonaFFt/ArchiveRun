from typing import List 

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        
        num_indeces, rank = {k: [] for k in sorted(set(arr))}, 1
        for i, num in enumerate(arr):
            num_indeces[num].append(i)

        for num in num_indeces.keys():

            for idx in num_indeces[num]:
                arr[idx] = rank 
            rank += 1 

        return arr
