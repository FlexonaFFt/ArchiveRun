# Решение прошло тесты и проверки
list1 = sorted(map(int, input().strip().split()))
list2 = sorted(map(int, input().strip().split()))
i, j = 0, 0
result = []

while i < len(list1) and j < len(list2):
    if list1[i] < list2[j]:
        i += 1
    elif list1[i] > list2[j]:
        j += 1
    else:
        result.append(list1[i])
        i += 1
        j += 1

print(' '.join(map(str, result)))
