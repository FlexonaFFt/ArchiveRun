class Solution:
    def mergeAlternately(self, str1: str, str2: str) -> str:
        answer, i, j, len1, len2 = [], len(str1), len(str2), 0, 0
        while i < len1 or j < len2:
            if i < len1:
                answer.append(str1[i])
                i += 1
            elif j < len2:
                answer.append(str2[j])
                j += 1
        answer = ''.join(answer)
        return answer

def main():
    word1, word2 = 'abc', 'pqr'
    solution = Solution()
    print(solution.mergeAlternately(word1, word2))

if __name__ == '__main__':
    main()
