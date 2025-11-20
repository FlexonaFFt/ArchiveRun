class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        cleaned = ''.join(char for char in s if char != '-').upper()
        parts, count = [], 0
        for char in reversed(cleaned):
            parts.append(char)
            count += 1
            if count == k:
                parts.append('-')
                count = 0


        if parts and parts[-1] == '-': parts.pop()
        result = ''.join(reversed(parts))
        return result
