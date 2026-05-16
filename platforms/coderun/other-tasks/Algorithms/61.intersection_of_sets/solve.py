# Код не проходит первый закрытый тест (id: 3)
def find_intersection_func(list1, list2):
    spisok, slovar = [], []
    for num in list1:
        if num not in slovar:
            slovar.append(num)
    for num in list2:
        if num in slovar:
            spisok.append(str(num))
    spisok = sorted(set(spisok))
    result = ' '.join(spisok)
    return result

def main():
    list1 = list(map(int, input().split()))
    list2 = list(map(int, input().split()))
    print(find_intersection_func(list1, list2))

if __name__ == '__main__':
    main()
