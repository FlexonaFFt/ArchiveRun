class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3: return False 

        vowels = set("aeiouAEIOU")
        has_vowels, has_cons = False, False 

        for c in word:
            if not c.isalnum(): return False 
            if c.isalpha():
                if c in vowels: has_vowels = True 
                else: has_cons = True 


        return has_cons and has_vowels


def test():
    solve = Solution()
    print(solve.isValid(word='234Adas'))
    print(solve.isValid(word="b3"))
    print(solve.isValid(word="a3$e"))

if __name__ == '__main__': test()
