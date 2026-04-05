class Solution:
    def judgeCircle(self, moves: str) -> bool:
        posx, posy = 0, 0  
        
        for move in moves:
            if move == 'R': posx += 1
            elif move == 'L': posx -= 1

            if move == 'U': posy += 1
            elif move == 'D': posy -= 1

        return True if posx == 0 and posy == 0 else False
