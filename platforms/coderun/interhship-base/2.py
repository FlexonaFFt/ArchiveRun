class Solution:

    def func(self, first: str, second: str) -> int:
        if sorted(first) == sorted(second):
            return 1
        else: return 0

    def main(self) -> None:
        str1 = str(input())
        str2 = str(input())
        print(self.func(str1, str2))


if __name__ == '__main__':
    Solution().main()