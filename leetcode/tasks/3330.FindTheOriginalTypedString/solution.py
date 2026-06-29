class Solution:
    def possibleStringCount(self, word: str) -> int:
        n, i, groups = len(word), 0, []
        while i < n:
            j = i
            while j < n and word[j] == word[i]:
                j += 1
            groups.append(j - i)
            i = j 

        result = 1 
        for length in groups: result += (length - 1)
        return result 


def test():
    solve = Solution()
    print(solve.possibleStringCount("abbcccc"))
    print(solve.possibleStringCount("abcd"))
    print(solve.possibleStringCount("aaaa"))


if __name__ == '__main__': test()
