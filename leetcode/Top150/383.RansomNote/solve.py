from collections import Counter 

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom = Counter(ransomNote)
        maag = Counter(magazine)
        return ransom <= maag


        '''
        return all(ransomNote.count(c) <= magazine.count(c) for c in set(ransomNote))
        '''
