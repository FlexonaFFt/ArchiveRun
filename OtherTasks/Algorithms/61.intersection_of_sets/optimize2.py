def mainfunc():
    list1 = set(map(int, input().split()))
    list2 = set(map(int, input().split()))
    result = sorted(list1 & list2)
    print(' '.join(map(str, result)))

if __name__ == '__main__':
    mainfunc()
