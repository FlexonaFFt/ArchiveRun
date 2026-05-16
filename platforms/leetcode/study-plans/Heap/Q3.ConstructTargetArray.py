import heapq
class Solution:
    def isPossible(self, target: List[int]) -> bool:
        n = len(target)
        if n == 1:
            return target[0] == 1

        heap = [-x for x in target]
        heapq.heapify(heap)
        total = sum(target)

        while True:
            m = -heapq.heappop(heap)   
            rest = total - m           

            if m == 1 or rest == 1:
                heapq.heappush(heap, -1)
                total = rest + 1
                if -heap[0] == 1: 
                    return True
                continue

            if rest == 0 or rest >= m:
                return False

            new = m % rest
            if new == 0:
                return False

            total = rest + new
            heapq.heappush(heap, -new)
            if -heap[0] == 1 and total == len(heap):
                return True

