from collections import Counter 

class Solution:

    def func(self, word: str) -> str: 
        counter = Counter()

        for char in word.split():
            counter.update(a + b for a, b in zip(char, char[1:]))
        return max(counter, key=lambda p: (counter[p], p))

    def main(self) -> None:
        string = str(input())
        print(self.func(string))


if __name__ == '__main__':
    Solution().main()