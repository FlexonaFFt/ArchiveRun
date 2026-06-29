def solution(n, t, a, b):
    events_one = [0] * (t + 2)
    events_two = [0] * (t + 2)
    total_one = 0
    total_two = 0

    for i in range(n):
        total_one += a[i]
        if b[i] > 0:
            total_two += b[i]
            if a[i] == 0:
                j_i = 0
            else:
                j_i = (a[i] + b[i] - 1) // b[i]
            if j_i <= t:
                events_one[j_i] += a[i]
                events_two[j_i] += b[i]

    res = [0] * (t + 1)
    res[0] = total_one

    F = events_one[0]
    H = events_two[0]
    for j in range(1, t + 1):
        F += events_one[j]
        H += events_two[j]
        G_j = total_two - H
        S_j = j * G_j + F
        res[j] = total_one - S_j

    return res
