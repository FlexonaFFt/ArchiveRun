from collections import deque, Counter
queue, heigh_counter = deque(), Counter()
n, total_height, result = int(input()), 0, []

for i in range(n):
    parts = input().split()
    if parts[0] == '+':
        chislo = int(parts[1])
        queue.append(chislo)
        heigh_counter[chislo] += 1
        total_height += chislo

    else:
        left = queue.popleft()
        heigh_counter[left] -= 1
        if heigh_counter[left] == 0: del heigh_counter[left]
        total_height -= left

    if queue:
        q_len = len(queue)
        if total_height % q_len == 0:
            avg = total_height // q_len
            result.append(str(heigh_counter.get(avg, 0)))
        else: result.append("0")
    else: result.append("0")

print('\n'.join(result))
