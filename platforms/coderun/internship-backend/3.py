class MySolution:

    def func(self, n: int, k: int, spisok: list[int]):
        result, curr = [], [] 

        for idx, right in enumerate(spisok):
            curr.append(right)

            while len(curr) > k: curr.pop(0)
            if idx >= k - 1: result.append(min(curr))
        return result


    def main(self) -> None:
        n, k = map(int, input().split())
        spisok = list(map(int, input().split()))
        output = self.func(n, k, spisok)
        for element in output:
            print(element)


if __name__ == '__main__':
    MySolution().main()