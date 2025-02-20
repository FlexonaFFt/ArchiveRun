class Solution:
    def mergeAlternately(self, str1: str, str2: str) -> str:
        answer = []
        len1, len2 = len(str1), len(str2)
        i, j = 0, 0

        while i < len1 or j < len2:
            if i < len1:
                answer.append(str1[i])
                i += 1
            if j < len2:
                answer.append(str2[j])
                j += 1

        return ''.join(answer)


# Runtime 41 ms, 27.62 %
# Memory 17.87 mb, 17.09 %
def main():
    solution = Solution()
    print(solution.mergeAlternately('abc', 'pqr'))  # Ожидаемый вывод: "apbqcr"
    print(solution.mergeAlternately('ab', 'pqrs'))  # Ожидаемый вывод: "apbqrs"
    print(solution.mergeAlternately('abcd', 'pq'))  # Ожидаемый вывод: "apbqcd"

if __name__ == '__main__':
    main()

