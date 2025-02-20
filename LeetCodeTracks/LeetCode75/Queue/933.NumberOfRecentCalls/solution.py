from collections import deque

class RecentCounter:

    def __init__(self):
        self.queue = deque()

    def ping(self, t: int) -> int:
        self.queue.append(t)
        while self.queue[0] < t - 3000:
            self.queue.popleft()
        return len(self.queue)

# Runtime 24 ms, 93.26 %
# Memory 23.27, 15.53 %
def main():
    recentCounter = RecentCounter()
    print(recentCounter.ping(1))     # 1
    print(recentCounter.ping(100))   # 2
    print(recentCounter.ping(3001))  # 3
    print(recentCounter.ping(3002))  # 3

if __name__ == '__main__':
    main()
