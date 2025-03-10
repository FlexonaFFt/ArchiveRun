class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        vowels, result, n = {'a', 'e', 'i', 'o', 'u'}, 0, len(word)
        vowel_count, cons_count, left = 0, 0, 0
        vowel_freq = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

        for right in range(n):
            char = word[right]
            if char in vowels:
                vowel_freq[char] += 1
                if vowel_freq[char] == 1:
                    vowel_count += 1
            else:
                cons_count += 1

            while cons_count > k:
                left_char = word[left]
                if left_char in vowels:
                    vowel_freq[left_char] -= 1
                    if vowel_freq[left_char] == 0:
                        vowel_count -= 1
                else:
                    cons_count -= 1
                left += 1

            if vowel_count == 5 and cons_count == k:
                result += 1
        return result

# Прога не прошла 639 тест
def main():
    solution = Solution()
    print(solution.countOfSubstrings("aeioqq", 1))
    print(solution.countOfSubstrings("aeiou", 0))
    print(solution.countOfSubstrings("ieaouqqieaouqq", 1))

if __name__ == '__main__':
    main()
