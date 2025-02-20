from collections import defaultdict, deque
import sys

def parse_dependencies(file_content):
    dependencies = defaultdict(list)
    for line in file_content.splitlines():
        if '->' in line:
            parts = line.strip().split('->')
            if len(parts) < 2:
                continue
            package = parts[0].strip().strip('"')
            dep = parts[1].split('[')[0].strip().strip('"')
            dependencies[package].append(dep)
    return dependencies

def topological_sort(dependencies):
    in_degree = defaultdict(int)
    for u in dependencies:
        if u not in in_degree:
            in_degree[u] = 0
        for v in dependencies[u]:
            in_degree[v] += 1

    queue = deque([u for u in in_degree if in_degree[u] == 0])
    sorted_list = []

    while queue:
        u = queue.popleft()
        sorted_list.append(u)
        for v in dependencies.get(u, []):
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    return sorted_list

def inputfunc():
    with open('input.txt', 'r') as file:
        content = file.read()

    dependencies = parse_dependencies(content)
    sorted_packages = topological_sort(dependencies)
    for package in reversed(sorted_packages):
        print(package)

def main():
    import sys
    content = sys.stdin.read()

    dependencies = parse_dependencies(content)
    sorted_packages = topological_sort(dependencies)
    for package in reversed(sorted_packages):
        print(package)

if __name__ == '__main__':
    inputfunc()
