class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        n = len(s)
        if n < k: return False 

        total, found = 1 << k, 0
        mask, curr = total - 1, 0 
        seen = [False] * total

        for i, char in enumerate(s):
            curr = ((curr << 1) & mask) | (char == '1')
            if i >= k - 1:
                if not seen[curr]:
                    seen[curr] = True 
                    found += 1

                    if found == total:
                        return True 
        return False 
