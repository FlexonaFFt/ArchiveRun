# Всё равно превышен лимит времени
# # Превышает лимит времени на последнем закрытом тесте (id: 7)
def mainfunc():
    list1 = list(map(int, input().split()))
    list2 = list(map(int, input().split()))
    set2 = set(list2)
    result = sorted(num for num in set(list1) if num in set2)
    print(*result)

if __name__ == '__main__':
    mainfunc()
