def solution(n, a):
    result = [1]
    prev = None

    for i in range(n):
        options = [a[i], -a[i]]
        options.sort()
        if prev is None:
            chosen = min(options)
        else:
            valid = [x for x in options if x >= prev]
            if not valid:
                return [0] * (n + 1)
            chosen = min(valid)
        result.append(chosen)
        prev = chosen

    return result


def test():
    print(solution(n=5, a=[1, -1, -2, 3, 6]))


if __name__ == '__main__': test()
