class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, best, curr = 0, 0, {}

        for right, value in enumerate(s):
            curr[value] = curr.get(value, 0) + 1
            while curr[value] > 1:
                curr[s[left]] -= 1
                left += 1

            best = max(best, right - left + 1)

        return best 
