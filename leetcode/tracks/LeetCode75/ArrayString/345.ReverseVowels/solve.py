class Solution:
    def reverseVowels(self, string: str) -> str:
        # Оказывается "Y" может быть как гласной, так и согласнйо буквой
        vowels = 'aeiouAEIOU'
        vowels_in_word = [char for char in string if char in vowels]
        vowels_in_word.reverse()
        result, vowel_idx = [], 0
        for char in string:
            if char in vowels:
                result.append(vowels_in_word[vowel_idx])
                vowel_idx += 1
            else: 
                result.append(char)
        return ''.join(result)


# Runtime 11ms, 66.16 %
# Memory 18.96 mb, 16.54 % 
def main():
    solution = Solution()
    string = "IceCreAm"
    print(solution.reverseVowels(string))

if __name__ == '__main__':
    main()
