class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        text, out = list(text), 0

        while True:
            word = list('balloon')
            for char in word:

                found = False 
                for idx in range(len(text)):
                    if text[idx] == char:
                        text[idx] = '#'
                        found = True 
                        break 

                if not found:
                    return out

            out += 1  
