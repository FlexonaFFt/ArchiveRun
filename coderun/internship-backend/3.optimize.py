from collections import deque

class MySolution:

    def func(self, n: int, k: int, spisok: list[int]):
        deq, output = deque([]), []

        for i in range(n):

            while deq and spisok[deq[-1]] >= spisok[i]:
                deq.pop()

            deq.append(i)
            while deq[0] <= i - k:
                deq.popleft()
            if i >= k - 1:
                output.append(spisok[deq[0]])

        return output


    def main(self) -> None:
        n, k = map(int, input().split())
        spisok = list(map(int, input().split()))
        output = self.func(n, k, spisok)
        for element in output:
            print(element)


if __name__ == '__main__':
    MySolution().main()