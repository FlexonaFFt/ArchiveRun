def most_frequent(array):
    arr_counter = {}
    for num in array:
        if num in arr_counter:
            arr_counter[num] += 1
        else:
            arr_counter[num] = 1
    return max(arr_counter, key=arr_counter.get)

if __name__ == '__main__':
    array = list(map(int, input().split()))
    print(most_frequent(array))
