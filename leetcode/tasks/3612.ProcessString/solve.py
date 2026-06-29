class Solution:
    def processStr(self, s: str) -> str:
        result, n = [], len(s) 

        for i in range(n):
            curr = s[i]
            if curr == '*':
                if len(result) != 0:
                    result.pop()

            elif curr == '#': result.extend(result[:])
            elif curr == '%': result.reverse()
            elif 'a' <= curr <= 'z': result.append(curr)

        return ''.join(result)
