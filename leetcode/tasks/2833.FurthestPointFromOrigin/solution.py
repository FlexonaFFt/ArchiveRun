class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        left, right = moves.count('L'), moves.count('R')
        free = len(moves) - left - right 
        diff = abs(left - right)
        return diff + free
