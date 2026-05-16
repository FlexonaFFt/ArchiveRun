from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        if set(word1) != set(word2):
            return False
        # Проверяем частоты символов (не обязательно в одном порядке)
        freq1 = Counter(word1)
        freq2 = Counter(word2)
        return sorted(freq1.values()) == sorted(freq2.values())

# Runtime 75 ms, 94.16 %
# Memory 18.18 mb, 50.96 %
def main():
    word1, word2 = 'abc', 'bca'
    word3, word4 = 'a', 'aa'
    word5, word6 = 'cabbba', 'abbccc'
    solution = Solution()
    print(solution.closeStrings(word1, word2))
    print(solution.closeStrings(word3, word4))
    print(solution.closeStrings(word5, word6))

if __name__ == '__main__':
    main()
