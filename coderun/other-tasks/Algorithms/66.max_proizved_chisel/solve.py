def find_the_max_numbers_product(numbers):
    import heapq
    if len(numbers) < 2:
        return None
    max1 = max2 = float('-inf')
    min1 = min2 = float('inf')

    for number in numbers:
        if number > max1:
            max2 = max1
            max1 = number
        elif number > max2:
            max2 = number
        if number < min1:
            min2 = min1
            min1 = number
        elif number < min2:
            min2 = number

    positive_product = max1 * max2 if max2 != float('-inf') else float('-inf')
    negative_product = min1 * min2 if min2 != float('inf') else float('inf')
    if positive_product > negative_product:
        return max1, max2
    else:
        return min1, min2

def main():
    numbers = list(map(int, input().split()))
    rezult = find_the_max_numbers_product(numbers)
    if rezult:
        rezult1 = max(rezult[0], rezult[1])
        rezult2 = min(rezult[0], rezult[1])
        print(rezult2, rezult1)

if __name__ == '__main__':
    main()
