# Не решает задачу
def find_fires_cnt(birds):
    from math import atan2
    n = len(birds)
    birds.sort(key=lambda x: (x[1], -x[0]))
    shots, prev_x = 0, 0
    for x, y in birds:
        if x != prev_x:
            shots += 1
            prev_x = x
    return shots

def main():
    n = int(input())
    birds = []
    for _ in range(n):
        x, y = map(int, input().split())
        birds.append((x, y))
    print(find_fires_cnt(birds))

if __name__ == '__main__':
    main()
