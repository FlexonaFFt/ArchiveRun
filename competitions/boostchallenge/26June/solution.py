def solution(n, blocks):
    blocks.sort()
    left = 0
    max_in_window = 0

    for right in range(n):
        while blocks[right] - blocks[left] >= n:
            left += 1
        max_in_window = max(max_in_window, right - left + 1)

    return n - max_in_window


def test():
    n, blocks = 5, [2, 0, -3, 3, 6]
    print(solution(n, blocks))
    
    n, blocks = 1, [25]
    print(solution(n, blocks))

if __name__ == '__main__': 
    test()
