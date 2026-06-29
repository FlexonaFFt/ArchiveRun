class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, freq = 0, {}

        max_freq, answer = 0, 0
        for right, val in enumerate(s):
            freq[val] = freq.get(val, 0) + 1
            max_freq = max(max_freq, freq[val])
            window_size = right - left + 1

            while window_size - max_freq > k:
                left_char = s[left]
                freq[left_char] -= 1
                left += 1

                window_size = right - left + 1

            answer = max(answer, window_size)

        return answer 
