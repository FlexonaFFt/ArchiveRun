class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        counter, left, curr = 0, 0, {}

        for right, char in enumerate(s):
            curr[char] = curr.get(char, 0) + 1

            while len(curr) == 3:
                counter += len(s) - right
                curr[s[left]] -= 1
                if curr[s[left]] == 0:
                    del curr[s[left]]

                left += 1

        return counter 
