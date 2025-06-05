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


class Solution:
    def to_mask(self, fragment):
        mask = 0
        for c in set(fragment):
            mask |= 1 << (ord(c) - ord('C'))
        return mask

    def dna_marker_pairs(self, fragments):
        from array import array

        N = len(fragments)
        MAX_MASK = 1 << 10

        count, res = [0] * MAX_MASK, 0
        for fragment in fragments:
            count[self.to_mask(fragment)] += 1

        for m1 in range(MAX_MASK):
            if count[m1] == 0:
                continue
            for m2 in range(m1, MAX_MASK):
                if count[m2] == 0:
                    continue
                if m1 & m2:
                    if m1 == m2:
                        res += count[m1] * (count[m1] - 1) // 2
                    else:
                        res += count[m1] * count[m2]
        return res


if __name__ == '__main__':
    solution = Solution()
    n = int(input())
    fragments = [input().strip() for _ in range(n)]
    print(solution.dna_marker_pairs(fragments))
