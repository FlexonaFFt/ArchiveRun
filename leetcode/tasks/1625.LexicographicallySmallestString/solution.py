from collections import deque
class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        def add_element(t: str) -> str:
            array = list(t)
            for i in range(1, len(array), 2):
                array[i] = str((int(array[i]) + a) % 10)
            return ''.join(array)

        def rotate_element(t: str) -> str:
            k = b % len(t)
            if k == 0: return t
            return t[-k:] + t[:-k]

        q, best, visited = deque([s]), s, set([s])
        while q:
            curr = q.popleft()
            if curr < best: best = curr 
            nxt_add = add_element(curr)
            if nxt_add not in visited:
                visited.add(nxt_add)
                q.append(nxt_add)

            nxt_rot = rotate_element(curr)
            if nxt_rot not in visited:
                visited.add(nxt_rot)
                q.append(nxt_rot)
        
        return best 
