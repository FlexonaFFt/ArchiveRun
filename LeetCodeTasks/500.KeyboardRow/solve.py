class Solution:
    from typing import List
    def findWords(self, words: List[str]) -> List[str]:
        row1 = set('qwertyuiop')
        row2 = set('asdfghjkl')
        row3 = set('zxcvbnm')
        result = []
        for word in words:
            word_set = set(word.lower())
            if word_set <= row1 or word_set <= row2 or word_set <= row3:
                result.append(word)
        return result

# Runtime 0 ms, 100 %
# Memory 17.84 mb, 29.24 %
def main():
    solve = Solution()
    print(solve.findWords(["Hello", "Alaska", "Dad", "Peace"]))
    print(solve.findWords(['omk']))
    print(solve.findWords(["adsdf","sfd"]))

if __name__ == '__main__':
    main()
