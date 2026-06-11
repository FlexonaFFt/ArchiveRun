n = int(input())
slovar = {}
for _ in range(n):
    first, second = input().split()
    slovar[first] = second
    slovar[second] = first
word = input().strip()
print(slovar[word])