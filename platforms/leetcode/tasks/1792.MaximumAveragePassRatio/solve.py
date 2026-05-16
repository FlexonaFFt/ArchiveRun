import heapq
class Solution():
    def maxAverageRation(self, classes: list[list[int]], 
                         extraStudents: int) -> float:

        def positive(p, t):
            return (p + 1) / (t + 1) - p / t

        heap = [(-positive(p, t), p, t) for p, t in classes]
        heapq.heapify(heap)
        for _ in range(extraStudents):
            g, p, t = heapq.heappop(heap)
            p, t = p + 1, t + 1
            heapq.heappush(heap, (-positive(p, t), p, t))

        total = sum(p / t for _, p, t in heap)
        return total / len(classes)


def test():
    solve = Solution()
    print(solve.maxAverageRation([[1,2],[3,5],[2,2]], 2))
    print(solve.maxAverageRation([[2,4],[3,9],[4,5],[2,10]],4))

if __name__ == '__main__':
    test()
