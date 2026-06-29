class Solution:
    def findEvenNumbers(self, digits: list[int]) -> list[int]:
        from collections import Counter
        freq, res = Counter(digits), []
        for num in range(100, 1000, 2):
            parts = [num // 100, (num // 10) % 10, num % 10]
            count = Counter(parts)
            if all(freq[q] >= count[q] for q in count):
                res.append(num)
        return res

# Runtime 47 ms, 68.85 %
# Memory 17.89 mb, 65.57 %
