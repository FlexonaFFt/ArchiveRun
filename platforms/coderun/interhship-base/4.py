'''
class MySolution:

    def generator(self, left: int, right: int, current: str):
        if left == 0 and right == 0:
            print(current)
            return 

        if left > 0:
            self.generator(left - 1, right, current + "(")
        if right > left: 
            self.generator(left, right - 1, current + ")")

    def func(self) -> None: 
        n = int(input())
        self.generator(n, n, "")


if __name__ == '__main__':
    MySolution().func()
'''

import sys

# Решение проходит только на python, но не на PyPy
class MySolution:

    def generator(self, left: int, right: int):
        if left == 0 and right == 0:
            sys.stdout.write(''.join(self.buf) + '\n')
            return

        if left > 0:
            self.buf.append('(')
            self.generator(left - 1, right)
            self.buf.pop()
        if right > left:
            self.buf.append(')')
            self.generator(left, right - 1)
            self.buf.pop()

    def func(self) -> None:
        n = int(input())
        self.buf = []
        self.generator(n, n)


if __name__ == '__main__':
    MySolution().func()