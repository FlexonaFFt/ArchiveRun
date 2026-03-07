class Solution:
    def minFlips(self, s: str) -> int:
        concat, n = s + s, len(s)
        alt1, alt2 = [], []
        
        for i in range(2 * n):
            if i % 2 == 0:
                alt1.append('0')
                alt2.append('1')
            else:
                alt1.append('1')
                alt2.append('0')
        alt1 = ''.join(alt1)
        alt2 = ''.join(alt2)

        miss1 = miss2 = 0
        left, ans = 0, float('inf')

        for right in range(2 * n):
            if concat[right] != alt1[right]: miss1 += 1
            if concat[right] != alt2[right]: miss2 += 1
            if right - left + 1 > n:
                if concat[left] != alt1[left]: miss1 -= 1
                if concat[left] != alt2[left]: miss2 -= 1
                left += 1
            
            if right - left + 1 == n:
                ans = min(ans, miss1, miss2)
        
        return ans 
