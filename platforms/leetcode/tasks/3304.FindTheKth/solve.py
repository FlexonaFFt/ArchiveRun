class Solution:
    def kthCharacter(self, k: int) -> str:
        word = 'a'
        while len(word) < k:
            next_part = ''.join(
                    chr(((ord(c) - ord("a") + 1) % 26) + ord('a')) for c in word
                    )
            word += next_part
        return word[k - 1]


def test():
    solve = Solution()
    print(solve.kthCharacter(5))
    print(solve.kthCharacter(10))

if __name__ == '__main__':
    test()
