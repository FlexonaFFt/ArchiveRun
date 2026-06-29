from collections import Counter

class Solution:
    def longestBalanced(self, s: str) -> int:
        left, best, window = 0, 0, Counter()

        for right, value in enumerate(s):
            window[value] = window.get(value, 0) + 1

            while window and len(set(window.values())) != 1:
                window[s[left]] -= 1
                if window[s[left]] == 0:
                    del window[s[left]]

                left += 1

            best = max(best, right - left + 1)
        return best