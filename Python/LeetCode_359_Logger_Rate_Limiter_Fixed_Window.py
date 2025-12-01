# Time Complexity: O(1)
# Space Complexity: O(N)
class Logger:

    def __init__(self):
        # 儲存 {message: next_allowed_timestamp}
        self.next_allowed_time = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        
        # 1. 取得該訊息下次允許列印的時間
        # 如果訊息不在 map 中，get(message, 0) 會返回 0。
        # 0 必然 <= 任何有效的 timestamp，故第一次出現的訊息一定會被允許。
        next_time = self.next_allowed_time.get(message, 0)
        # 2. 檢查限制
        if timestamp < next_time:
            # 目前時間還在冷卻期內，不能列印
            return False
        
        # 3. 允許列印，更新下次允許列印的時間 (現在時間 + 3 秒)
        self.next_allowed_time[message] = timestamp + 3

        return True

# 舉例：
logger = Logger()
r = logger.shouldPrintMessage(1, "foo")  # True -> next_allowed_time["foo"] = 11
print(r)
r = logger.shouldPrintMessage(2, "bar")  # True -> next_allowed_time["bar"] = 12
print(r)
r = logger.shouldPrintMessage(3, "foo")  # False (3 < 11)
print(r)
# logger.shouldPrintMessage(11, "foo") # True (11 >= 11) -> next_allowed_time["foo"] = 21