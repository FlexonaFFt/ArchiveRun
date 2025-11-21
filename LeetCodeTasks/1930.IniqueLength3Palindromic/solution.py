class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        first, last, answer = [-1] * 26, [-1] * 26, 0
        for i, ch in enumerate(s):
            idx = ord(ch) - ord('a')
            if first[idx] == -1: first[idx] = i
            last[idx] = i

        for x in range(26):
            l, r = first[x], last[x]
            if l != -1 and r != -1 and r > l + 1:
                seen_middle = set()
                for i in range(l + 1, r): seen_middle.add(s[i])
                answer += len(seen_middle)
        
        return answer
