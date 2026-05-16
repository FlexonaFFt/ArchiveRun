import sys

def cnt_mod8(r: int) -> int:
    if r == 0:
        return 1
    rr = r * r
    y = r
    sumYParity = 0
    for x in range(1, r + 1):
        xx = x * x
        while y > 0 and xx + y * y > rr:
            y -= 1
        sumYParity ^= (y & 1)
    return (1 + 4 * sumYParity + 4 * (r & 1)) & 7

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    radii = [int(next(it)) for _ in range(n)]
    cache = {}
    total_mod8 = 0
    residues = []
    for r in radii:
        if r not in cache:
            cache[r] = cnt_mod8(r)
        v = cache[r]
        residues.append(v)
        total_mod8 = (total_mod8 + v) & 7
    if total_mod8 == 0:
        print(0)
        return
    freq = [0] * 8
    for v in residues:
        freq[v] += 1
    S = total_mod8
    if freq[S] > 0:
        print(1)
        return
    for a in range(8):
        b = (S - a) & 7
        if a == b:
            if freq[a] >= 2:
                print(2)
                return
        else:
            if freq[a] > 0 and freq[b] > 0:
                print(2)
                return
    for a in range(8):
        if freq[a] == 0:
            continue
        for b in range(8):
            if freq[b] == 0:
                continue
            for c in range(8):
                if freq[c] == 0:
                    continue
                if ((a + b + c) & 7) != S:
                    continue
                if a == b == c:
                    if freq[a] >= 3:
                        print(3)
                        return
                elif a == b:
                    if freq[a] >= 2 and freq[c] >= 1:
                        print(3)
                        return
                elif a == c:
                    if freq[a] >= 2 and freq[b] >= 1:
                        print(3)
                        return
                elif b == c:
                    if freq[b] >= 2 and freq[a] >= 1:
                        print(3)
                        return
                else:
                    print(3)
                    return
    for k in range(8):
        if freq[k] >= 4 and ((4 * k) & 7) == S:
            print(4)
            return
    total_count = sum(freq)
    if total_count >= 4:
        print(4)
    else:
        print(total_count)

if __name__ == "__main__":
    main()
