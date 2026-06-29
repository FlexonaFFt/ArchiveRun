class Solution:
    def clearDigits(self, s: str) -> str:
        translation_table = str.maketrans('', '', '1234567890')
        return s.translate(translation_table)


def main():
    solve = Solution()
    print(solve.clearDigits('abc'))
    print(solve.clearDigits('ab34'))

if __name__ == '__main__':
    main()
