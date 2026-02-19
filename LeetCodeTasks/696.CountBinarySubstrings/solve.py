class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        if len(s) < 2:
            return 0

        blocks = []
        counter = 1

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                counter += 1
            else:
                blocks.append(counter)
                counter = 1
        blocks.append(counter)

        out = 0
        for i in range(1, len(blocks)):
            out += min(blocks[i - 1], blocks[i])

        return out
