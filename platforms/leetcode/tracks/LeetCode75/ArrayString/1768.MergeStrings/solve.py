# Решение багается и не проходит некоторые проверки.
# Данный код не является решением.
class Solution:
    def mergeAlternately(self, str1: str, str2: str) -> str:
        answer, len1, len2 = [], len(str1), len(str2)
        max_len, min_len, ogranichitel = max(len1, len2), min(len1, len2), 0
        max_str, min_str = max(str1, str2, key=len), min(str1, str2, key=len)
        for i in range(max_len):
            if ogranichitel <= min_len:
                answer.append(max_str[i])
                answer.append(min_str[i])
                ogranichitel += 1
            else:
                answer.append(max_str)
        answer_str = ''.join(answer)
        return answer_str


def main():
    word1, word2 = 'abc', 'pqr'
    solution = Solution()
    print(solution.mergeAlternately(word1, word2))

if __name__ == '__main__':
    main()
