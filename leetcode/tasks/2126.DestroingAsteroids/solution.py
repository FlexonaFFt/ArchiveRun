from typing import List 

class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        
        sort_asteroids, status = sorted(asteroids), True
        for aster in sort_asteroids:
            if mass > aster or mass == aster: mass += aster
            else: return False 

        return status
