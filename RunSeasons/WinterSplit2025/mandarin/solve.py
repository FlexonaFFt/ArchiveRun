def solve(n, boxes, total_mandarins, total_oranges):
    needed_mandarins = total_mandarins // 2
    needed_oranges = total_oranges // 2
    boxes.sort(key=lambda x: abs(x[0] - x[1]), reverse=True)
    selected_mandarins = sum(box[0] for box in boxes[:n])
    selected_oranges = sum(box[1] for box in boxes[:n])
    if selected_mandarins >= needed_mandarins and selected_oranges >= needed_oranges:
        return "YES"
    else:
        return "NO"

def main():
    n = int(input())
    boxes = []
    total_mandarins, total_oranges = 0, 0
    for i in range(n):
        m, o = map(int, input().split())
        boxes.append((m, o))
        total_mandarins += m 
        total_oranges += o
    print(solve(n, boxes, total_mandarins, total_oranges))

if __name__ == '__main__':
    main()