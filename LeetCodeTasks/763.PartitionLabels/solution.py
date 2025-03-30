class Solution:
    def partitionLabels(self, s: str) -> list[int]:

        # Отслеживаем последнее вхождение символа
        occurrence, result = {}, []
        for i, char in enumerate(s):
            occurrence[char] = i

        start, end = 0, 0
        for i, char in enumerate(s):
            end = max(end, occurrence[char])
            if i == end:
                result.append(end - start + 1)
                start = i + 1
        return result

# Runtime 5 ms, 54.86 %
# Memory 17.84 mb, 36.45 %
def main():
    solution = Solution()
    print(solution.partitionLabels(s="ababcbacadefegdehijhklij"))
    print(solution.partitionLabels(s="eccbbbbdec"))

main()
