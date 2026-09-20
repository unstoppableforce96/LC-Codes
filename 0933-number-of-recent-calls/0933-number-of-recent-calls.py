class RecentCounter:

    def __init__(self):
        self.q = Deque()
        self.counter = 0

    def ping(self, t: int) -> int:
        while self.q and self.q[0] < t - 3000:
            self.q.popleft()
            self.counter -= 1
        self.q.append(t)
        self.counter += 1
        return self.counter


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)