from collections import deque

class SlidingWindowRateLimiter:
    def __init__(self, max_requests=10, window_size=60):
        self.requests = {}  # user_id -> deque of timestamps
        self.max_requests = max_requests
        self.window_size = window_size

    def is_allowed(self, user_id, timestamp):
        if user_id not in self.requests:
            self.requests[user_id] = deque()

        q = self.requests[user_id]

        # 移除過期時間戳
        while q and q[0] <= timestamp - self.window_size:
            q.popleft()

        if len(q) < self.max_requests:
            q.append(timestamp)
            return True
        else:
            return False
