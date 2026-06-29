class SmallestInfiniteSet:

    def __init__(self):
        self.next_num = 1
        self.heap = [] 
        self.in_heap = set()

    def popSmallest(self) -> int:
        if self.heap:
            num = heapq.heappop(self.heap)
            self.in_heap.remove(num)
            return num 

        num = self.next_num
        self.next_num += 1
        return num 

    def addBack(self, num: int) -> None:
        if num < self.next_num and num not in self.in_heap:
            heapq.heappush(self.heap, num)
            self.in_heap.add(num)

