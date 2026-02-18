class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        string, oper = str(bin(n)[2:]), True 
        for i in range(1, len(string)): 
            if string[i] == string[i - 1]:
                oper = False 

        return oper
