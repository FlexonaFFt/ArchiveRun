class Solution:
    def numberOfPairs(self, points: list[list[int]]) -> int:
        n, counter = len(points), 0
        for i in range(n):
            for j in range(n):
                if i == j: continue 
                x1, y1 = points[i]
                x2, y2 = points[j]

                if x1 < x2 and y1 > y2:
                    valid = True 
                    for k in range(n):
                        if k == i or k == j: continue 
                        x, y = points[k]
                        if x1 <= x <= x2 and y2 <= y <= y1:
                            valid = False 
                            break 
                    if valid: counter += 1

        return counter 


def test():
    solve = Solution()
    print(solve.numberOfPairs([[1,1],[2,2],[3,3]]))
    print(solve.numberOfPairs([[6,2],[4,4],[2,6]]))
    print(solve.numberOfPairs([[3,1],[1,3],[1,1]]))

if __name__ == '__main__':
    test()
