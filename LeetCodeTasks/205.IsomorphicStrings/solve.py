class Solution:
    from typing import List
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sTable, tTable = {}, {}
        for s_char, t_char in zip(s, t):
            if s_char in sTable:
                if sTable[s_char] != t_char:
                    return False
            else:
                if t_char in tTable:
                    return False
                sTable[s_char] = t_char
                tTable[t_char] = s_char
        return True

# Runtime 3 ms, 96.24 %
# Memory 18.10 mb, 32.61 %
def main():
    solve = Solution()
    print(solve.isIsomorphic('egg', 'edd'))
    print(solve.isIsomorphic('foo', 'bar'))
    print(solve.isIsomorphic('paper', 'title'))

if __name__ == '__main__':
    main()
