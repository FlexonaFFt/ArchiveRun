class Solution:
    def maxVowels(self, string: str, k: int) -> int:
        current_count, max_count = 0, 0
        vowels = 'aeiou'
        for i in range(k):
            if string[i] in vowels:
                current_count += 1
        max_count = current_count
        for i in range(k, len(string)):
            if string[i] in vowels:
                current_count += 1
            if string[i - k] in vowels:
                current_count -= 1
            max_count = max(max_count, current_count)
        return max_count

# Runtime 69 ms, 83.40 %
# Memory 18 mb, 38.84 %
def main():
    string, k = "abciiidef", 3
    solution = Solution()
    print(solution.maxVowels(string, k))

if __name__ == '__main__':
    main()
