class Solution:
    def minimumDeletions(self, s: str) -> int:
        countA, countB = 0, 0
        for element in s:
            if element == 'a': countA += 1

        output = min(countA, len(s) - countA)
        for element in s:
            if element == 'a':
                countA -= 1
            else: countB += 1

            output = min(output, countB + countA)
        return output
