class Solution:
    from typing import List
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            while stack and asteroid < 0 < stack[-1]:
                if stack[-1] < -asteroid:
                    stack.pop()
                    continue
                elif stack[-1] == -asteroid:
                    stack.pop()
                break
            else:
                stack.append(asteroid)
        return stack

# Runtime 5 ms, 72.74 %
# Memory 18.84 mb, 39.79 %
def main():
    solution = Solution()
    asteroids1 = [5,10,-5]
    asteroids2 = [8, -8]
    asteroids3 = [10,2,-5]
    print(solution.asteroidCollision(asteroids1))
    print(solution.asteroidCollision(asteroids2))
    print(solution.asteroidCollision(asteroids3))

if __name__ == '__main__':
    main()
