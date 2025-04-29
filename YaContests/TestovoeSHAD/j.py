import sys
from collections import deque

class Solution:
    def solve(self, K: int, N: int, spisok: list[int]) -> int: # type: ignore
        if K == 1:
            print(max(x * x for x in spisok))
            return # type: ignore

        max_product = -float('inf')
        min_deque = deque()
        max_deque = deque()

        for i in range(N):
            while min_deque and min_deque[0] <= i - K:
                min_deque.popleft()
            while max_deque and max_deque[0] <= i - K:
                max_deque.popleft()

            while min_deque and spisok[min_deque[-1]] >= spisok[i]:
                min_deque.pop()
            min_deque.append(i)

            while max_deque and spisok[max_deque[-1]] <= spisok[i]:
                max_deque.pop()
            max_deque.append(i)

            if i >= K - 1:
                current_min = spisok[min_deque[0]]
                current_max = spisok[max_deque[0]]
                max_product = max(max_product, current_min * current_max)

        print(max_product)

def main():
    N, K = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    solution = Solution()
    solution.solve(N=N, K=K, spisok=a)


def test():
    solution = Solution()
    solution.solve(N=4, K=2, spisok=[1, 4, 3, 5])
    solution.solve(N=5, K=2, spisok=[-10, -9, 10, 1, 80])
    solution.solve(N=4, K=2, spisok=[1, 2, 1, 1, 1])
    solution.solve(N=5, K=3, spisok=[-10, -9, 10, 1, 80])

if __name__ == '__main__':
    test()
