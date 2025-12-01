import time

class TokenBucket:
    def __init__(self, rate, capacity):
        self.rate = rate          # token 產生速率（token/秒）
        self.capacity = capacity  # 桶子容量
        self.tokens = capacity    # 當前 token 數量
        self.timestamp = time.time()

    def allow_request(self):
        now = time.time()
        # 補充 token
        delta = now - self.timestamp
        self.tokens = min(self.capacity, self.tokens + delta * self.rate)
        self.timestamp = now

        if self.tokens >= 1:
            self.tokens -= 1
            return True
        else:
            return False
