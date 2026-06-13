n = int(input())
spisok = []

for _ in range(n):
    spisok.append(int(input()))
output = set(spisok)
for curr in output:
    print(curr)