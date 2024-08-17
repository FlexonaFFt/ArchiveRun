def find_partitions(n, max_num, current_partition, all_partitions):
    if n == 0:
        all_partitions.append(tuple(current_partition))
        return
    for i in range(min(n, max_num), 0, -1):
        current_partition.append(i)
        find_partitions(n - i, i, current_partition, all_partitions)
        current_partition.pop()

def print_partitions(n):
    all_partitions = []
    find_partitions(n, n, [], all_partitions)
    all_partitions.sort(key=lambda x: (sum(x), x))
    for partition in all_partitions:
        print(" + ".join(map(str, partition)))

if __name__ == "__main__":
    N = int(input().strip())
    print_partitions(N)
