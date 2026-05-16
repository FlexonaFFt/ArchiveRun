def solution(n, blocks):
    blocks.sort()
    moves = 0
    for i in range(len(blocks)):
        moves += abs(blocks[i] - (blocks[0] + i))
    return moves


def test():
    n, blocks = 5, [2, 0, -3, 3, 6]
    print(solution(n, blocks))

    n, blocks = 1, [25]
    print(solution(n, blocks))

if __name__ == '__main__': test()
