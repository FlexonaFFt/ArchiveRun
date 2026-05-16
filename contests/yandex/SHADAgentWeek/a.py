class Solution:

    def inputer(self):
        n, q = map(int, input().split())
        spisok = list(map(int, input().split()))
        return n, q, spisok

    def main(self):
        n, q, spisok = self.inputer()
        diffs, counter, curr = [0] * (n + 2), [], 0

        for _ in range(q):
            l, r = map(int, input().split())
            diffs[l] += 1
            diffs[r + 1] -= 1

        for i in range(1, n + 1):
            curr += diffs[i]
            counter.append(curr)

        counter.sort(reverse=True)
        spisok.sort(reverse=True)
        return sum(c * v for c, v in zip(counter, spisok))


if __name__ == '__main__':
    print(Solution().main())