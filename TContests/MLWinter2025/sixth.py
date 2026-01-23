import random


class Node:
    __slots__ = ("ch", "length", "prio", "left", "right", "size", "lazy")

    def __init__(self, ch, length, prio, left=None, right=None):
        self.ch = ch
        self.length = length
        self.prio = prio
        self.left = left
        self.right = right
        self.lazy = 1
        self.size = length + (left.size if left else 0) + (right.size if right else 0)


def node_size(node):
    return node.size if node else 0


def apply_mul(node, mul):
    if node:
        node.length *= mul
        node.size *= mul
        node.lazy *= mul


def push(node):
    if node and node.lazy != 1:
        apply_mul(node.left, node.lazy)
        apply_mul(node.right, node.lazy)
        node.lazy = 1


def update(node):
    node.size = node.length + node_size(node.left) + node_size(node.right)


def merge(a, b):
    if not a:
        return b
    if not b:
        return a
    if a.prio > b.prio:
        push(a)
        a.right = merge(a.right, b)
        update(a)
        return a
    push(b)
    b.left = merge(a, b.left)
    update(b)
    return b


def split(node, k):
    if not node:
        return None, None
    push(node)
    left_size = node_size(node.left)
    if k < left_size:
        left_part, right_part = split(node.left, k)
        node.left = right_part
        update(node)
        return left_part, node
    if k > left_size + node.length:
        left_part, right_part = split(node.right, k - left_size - node.length)
        node.right = left_part
        update(node)
        return node, right_part

    left_len = k - left_size
    right_len = node.length - left_len
    if left_len == 0:
        left_part = node.left
        node.left = None
        update(node)
        return left_part, node
    if right_len == 0:
        right_part = node.right
        node.right = None
        update(node)
        return node, right_part

    left_node = Node(node.ch, left_len, node.prio, node.left, None)
    right_node = Node(node.ch, right_len, node.prio, None, node.right)
    return left_node, right_node


def get_char(node, idx):
    while True:
        push(node)
        left_size = node_size(node.left)
        if idx < left_size:
            node = node.left
        elif idx >= left_size + node.length:
            idx -= left_size + node.length
            node = node.right
        else:
            return node.ch


class Solution:
    def process(self, s, queries):
        random.seed(0)
        root = None
        i = 0
        n = len(s)
        while i < n:
            j = i + 1
            while j < n and s[j] == s[i]:
                j += 1
            node = Node(s[i], j - i, random.randrange(1 << 30))
            root = merge(root, node)
            i = j

        out = []
        for q in queries:
            if q[0] == 1:
                l, r = q[1], q[2]
                left, rest = split(root, l - 1)
                mid, right = split(rest, r - l + 1)
                apply_mul(mid, 2)
                root = merge(merge(left, mid), right)
            else:
                out.append(get_char(root, q[1] - 1))
        return out


if __name__ == "__main__":
    n, q = map(int, input().split())
    s = input().strip()
    queries = []
    for _ in range(q):
        parts = input().split()
        if parts[0] == "1":
            queries.append([1, int(parts[1]), int(parts[2])])
        else:
            queries.append([2, int(parts[1])])

    solver = Solution()
    result = solver.process(s, queries)
    if result:
        print("\n".join(result))
