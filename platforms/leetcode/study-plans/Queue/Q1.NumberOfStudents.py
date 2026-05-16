from collections import deque
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        q = deque(students)
        s = deque(sandwiches)
        rotations_without_eat = 0

        while q and s:
            if q[0] == s[0]:
                q.popleft()
                s.popleft()
                rotations_without_eat = 0
            else:
                q.append(q.popleft())
                rotations_without_eat += 1
                if rotations_without_eat == len(q):
                    break

        return len(q)
