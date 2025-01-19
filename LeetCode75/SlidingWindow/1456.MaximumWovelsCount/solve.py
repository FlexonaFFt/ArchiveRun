class Solution:
    def maxVowels(self, string: str, k: int) -> int:
        def slidiing_window(s, window):
            for i in range(len(s) - window + 1):
                yield s[i:i + window]

        current_count, max_count = 0, 0
        vowels = 'aeiou'
        for window in slidiing_window(string, k):
            for char in window:
                if char in vowels:
                    current_count += 1
            if current_count > max_count:
                max_count = current_count
            current_count = 0
        return max_count

# TimeLimit 103 тест
def main():
    string, k = "abciiidef", 3
    solution = Solution()
    print(solution.maxVowels(string, k))

if __name__ == '__main__':
    main()
