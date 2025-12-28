from typing import List 

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        counter = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] < 0:
                    counter += 1
        return counter
