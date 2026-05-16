class Solution:
    from typing import List
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_dict = {char: idx for idx, char in enumerate(order)}

        def compare(word1: str, word2: str) -> int:
            i = 0
            while i < len(word1) and i < len(word2):
                if order_dict[word1[i]] < order_dict[word2[i]]:
                    return -1
                elif order_dict[word1[i]] > order_dict[word2[i]]:
                    return 1
                i += 1
            return -1 if len(word1) < len(word2) else 1 if len(word1) > len(word2) else 0

        for i in range(len(words) - 1):
            if compare(words[i], words[i + 1]) > 0:
                return False
        return True

# Runtime 0 ms, 100 %
# Memory 17.80 mb, 73.19 %
def main():
    solution = Solution()
    print(solution.isAlienSorted(words=["hello","leetcode"], order="hlabcdefgijkmnopqrstuvwxyz"))
    print(solution.isAlienSorted(words=["word","world","row"], order="worldabcefghijkmnpqstuvxyz"))
    print(solution.isAlienSorted(words=["apple","app"], order="abcdefghijklmnopqrstuvwxyz"))

if __name__ == '__main__':
    main()
