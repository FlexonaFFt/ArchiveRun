class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for char in ransomNote:
            if char in magazine:
                ransomNote = ransomNote.replace(char, "", 1)
                magazine = magazine.replace(char, "", 1)
        if ransomNote == '':
            return True
        return False

# Runtime 7 ms,  92 %
# Memory 17.95 mb, 54.27 %
def main():
    solution = Solution()
    print(solution.canConstruct("a", "b"))
    print(solution.canConstruct("aa", "ab"))
    print(solution.canConstruct("aa", "aab"))

if __name__ == '__main__':
    main()
