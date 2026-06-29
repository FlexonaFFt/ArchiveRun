class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.isupper():
            return True

        if word.islower():
            return True

        if len(word) >= 2 and word[0].isupper() and word[1:].islower():
            return True
        return False 
