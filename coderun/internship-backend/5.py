class Solution:

    def main(self, n, m, coords, bools):
        events, counter, out = [], 0, [0] * m
        for left, right in coords:
            a, b = min(left, right), max(left, right)
            events.append((a, 0))
            events.append((b, 2)) 

        for i, x in enumerate(bools):
            events.append((x, 1, i))

        # сортируем точки и перебираем
        events.sort()
        for event in events:
            if event[1] == 0: counter += 1
            elif event[1] == 2: counter -= 1
            else: out[event[2]] = counter 

        return out


    def inputer(self) -> None: 
        n, m = map(int, input().split())
        coords, bools = [], [] 
        for _ in range(n):
            coords.append(list(map(int, input().split())))
        bools = list(map(int, input().split()))

        print(*self.main(n, m, coords, bools))



if __name__ == '__main__':
    Solution().inputer()