'''
from collections import Counter
class Solution:
    def to_mask(self, fragment):
        mask = 0
        for char in set(fragment): mask |= 1 << (ord(char) - ord("C"))
        return mask

    def dna_marker_pairs(self, fragmets):
        mask_counts = Counter()
        for fragment in fragmets:
            mask = self.to_mask(fragment)
            mask_counts[mask] += 1

        total = sum(mask_counts.values())
        total_pairs = total * (total - 1) // 2
        masks, dsj = list(mask_counts.keys()), 0
        for i in range(len(masks)):
            for j in range(i + 1, len(masks)):
                if masks[i] & masks[j] == 0: dsj += mask_counts[masks[i]] * mask_counts[masks[j]]
        return total_pairs - dsj


if __name__ == '__main__':
    solution = Solution()
    n = int(input())
    fragments = [input().strip() for _ in range(n)]
    print(solution.dna_marker_pairs(fragmets=fragments))'''


from sys import stdin
from collections import defaultdict

def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    n = int(data[0])
    fragments = data[1:]
    mask_count = defaultdict(int)

    for frag in fragments:
        mask = 0
        for c in frag:
            mask |= 1 << (ord(c) - ord('C'))
        mask_count[mask] += 1

    total = n * (n - 1) // 2
    disjoint_pairs = 0
    masks = list(mask_count.keys())
    for i in range(len(masks)):
        m1 = masks[i]
        cnt1 = mask_count[m1]
        if cnt1 == 0:
            continue
        for j in range(i, len(masks)):
            m2 = masks[j]
            cnt2 = mask_count[m2]
            if (m1 & m2) == 0:
                if m1 == m2:
                    disjoint_pairs += cnt1 * (cnt1 - 1) // 2
                else:
                    disjoint_pairs += cnt1 * cnt2

    print(total - disjoint_pairs)

if __name__ == "__main__":
    main()
