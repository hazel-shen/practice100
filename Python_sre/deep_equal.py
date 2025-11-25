def deepEqual(obj1, obj2):
    """
    判斷兩個 JSON 物件是否完全相等
    需要遞迴比較所有巢狀結構
    """
    if type(obj1) != type(obj2):
        return False

    # dict 比較
    if isinstance(obj1, dict):
        if set(obj1.keys()) != set(obj2.keys()):
            return False
        for key in obj1:
            if not deepEqual(obj1[key], obj2[key]):
                return False
        return True
    
    # list 比較
    if isinstance(obj1, list):
        if len(obj1) != len(obj2):
            return False
        for i in range(len(obj1)):
            if not deepEqual(obj1[i], obj2[i]):
                return False
        return True
    return obj1 == obj2


# 測試
print(deepEqual(
    {"a": 1, "b": {"c": 2}},
    {"a": 1, "b": {"c": 2}}
))  # True

print(deepEqual(
    {"a": 1, "b": {"c": 2}},
    {"a": 1, "b": {"c": 3}}
))  # False

print(deepEqual(
    [1, 2, [3, 4]],
    [1, 2, [3, 4]]
))  # True

print(deepEqual(
    {"a": [1, 2], "b": 3},
    {"b": 3, "a": [1, 2]}
))  # True (順序不同但相等)