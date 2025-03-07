class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        spisok, result = [], False
        for char in s:
            spisok.append(char)
        for char in t:
            if char in spisok:
                result = True
                spisok.remove(char)
            else:
                result = False
                break
        return result

# Runtime 903 ms, 5 %
# Memory 18.37 mb, 22.41 %
def main():
    solution = Solution()
    print(solution.isAnagram(s="anagram", t="nagaram"))
    print(solution.isAnagram(s="rat", t="car"))

if __name__ == '__main__':
    main()
