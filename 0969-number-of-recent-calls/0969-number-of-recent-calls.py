class RecentCounter:

    def __init__(self):
        self.q=deque()

    def ping(self, t: int) -> int:
        front=t-3000
        while self.q and front>self.q[0]:
            self.q.popleft()
        self.q.append(t)
        return len(self.q)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)