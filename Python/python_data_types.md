# Python 常用資料類型速查表 🐍

## 📋 基本資料類型

### 1. 數值型別 (Numeric)

#### int (整數)

```python
x = 42
y = -17
z = 0
```

#### float (浮點數)

```python
pi = 3.14
temp = -273.15
```

#### complex (複數)

```python
c = 3 + 4j
```

---

## 📝 字串 (String)

### 基本操作

```python
# 宣告
s = "Hello"
s2 = 'World'
multi = """多行
字串"""

# 常用方法
s.upper()           # "HELLO"
s.lower()           # "hello"
s.strip()           # 去除空白
s.split(',')        # 分割字串
s.replace('l', 'L') # 替換
len(s)              # 長度

# 格式化
name = "Alice"
f"Hello {name}"     # f-string (推薦)
"Hello {}".format(name)
```

### 常用操作

```python
# 索引與切片
s[0]        # 第一個字元
s[-1]       # 最後一個字元
s[1:4]      # 切片 [1, 4)
s[::-1]     # 反轉字串

# 判斷
s.startswith('He')  # True
s.endswith('lo')    # True
'ell' in s          # True
```

---

## 📚 串列 (List)

### 特性

- **可變 (Mutable)**
- 有序
- 允許重複

### 基本操作

```python
# 宣告
lst = [1, 2, 3, 4, 5]
mixed = [1, "two", 3.0, [4, 5]]

# 新增
lst.append(6)       # 尾端加入
lst.insert(0, 0)    # 指定位置插入
lst.extend([7, 8])  # 合併列表

# 刪除
lst.pop()           # 移除最後一個
lst.pop(0)          # 移除指定索引
lst.remove(3)       # 移除指定值
del lst[1]          # 刪除指定位置

# 查詢
lst.index(5)        # 找到值的索引
lst.count(2)        # 計算出現次數
len(lst)            # 長度

# 排序
lst.sort()          # 原地排序
sorted(lst)         # 回傳新排序列表
lst.reverse()       # 反轉
```

### List Comprehension (超實用!)

```python
# 基本形式
squares = [x**2 for x in range(10)]

# 帶條件
evens = [x for x in range(10) if x % 2 == 0]

# 巢狀
matrix = [[i+j for j in range(3)] for i in range(3)]
```

---

## 📦 元組 (Tuple)

### 特性

- **不可變 (Immutable)**
- 有序
- 比 List 快

### 基本操作

```python
# 宣告
t = (1, 2, 3)
single = (1,)       # 單元素要加逗號
t2 = 1, 2, 3        # 可省略括號

# 操作
t[0]                # 索引
t.count(2)          # 計數
t.index(3)          # 查找
len(t)              # 長度

# 解包 (Unpacking)
a, b, c = t
x, *rest = (1, 2, 3, 4)  # x=1, rest=[2,3,4]
```

### 使用時機

```python
# 當作 dictionary 的 key
pos = {(0, 0): "origin", (1, 1): "diagonal"}

# 函數回傳多個值
def get_coords():
    return (10, 20)
```

---

## 🗂️ 字典 (Dictionary)

### 特性

- **可變 (Mutable)**
- Key-Value 對應
- Key 必須是不可變類型

### 基本操作

```python
# 宣告
d = {"name": "Alice", "age": 25}
d2 = dict(name="Bob", age=30)

# 存取
d["name"]           # 取值
d.get("name")       # 安全取值
d.get("job", "N/A") # 提供預設值

# 新增/修改
d["city"] = "Taipei"
d.update({"age": 26, "job": "Engineer"})

# 刪除
del d["age"]
d.pop("city")       # 回傳被刪除的值
d.clear()           # 清空

# 查詢
"name" in d         # 檢查 key
d.keys()            # 所有 keys
d.values()          # 所有 values
d.items()           # 所有 (key, value) 對
```

### 常用模式

```python
# 遍歷
for key, value in d.items():
    print(f"{key}: {value}")

# Dictionary Comprehension
squares = {x: x**2 for x in range(5)}

# 預設值處理
from collections import defaultdict
dd = defaultdict(int)  # 預設值為 0
dd = defaultdict(list) # 預設值為 []
```

---

## 🎯 集合 (Set)

### 特性

- **可變 (Mutable)**
- 無序
- 元素唯一 (自動去重)

### 基本操作

```python
# 宣告
s = {1, 2, 3, 4}
s2 = set([1, 2, 2, 3])  # {1, 2, 3}
empty = set()           # 注意:不是 {}

# 新增/刪除
s.add(5)
s.remove(1)      # 不存在會報錯
s.discard(1)     # 不存在不報錯
s.pop()          # 隨機移除

# 集合運算
a = {1, 2, 3}
b = {3, 4, 5}

a | b            # 聯集 {1,2,3,4,5}
a & b            # 交集 {3}
a - b            # 差集 {1,2}
a ^ b            # 對稱差集 {1,2,4,5}

# 判斷
a.issubset(b)    # a 是否為 b 的子集
a.issuperset(b)  # a 是否包含 b
```

### 使用時機

```python
# 去重
unique = list(set([1, 2, 2, 3, 3]))

# 檢查成員(比 list 快)
valid_users = {"alice", "bob", "charlie"}
if user in valid_users:
    print("Valid!")
```

---

## 🆚 快速比較表

| 類型      | 可變 | 有序 | 重複 | 索引 | 使用場景            |
| --------- | ---- | ---- | ---- | ---- | ------------------- |
| **List**  | ✅   | ✅   | ✅   | ✅   | 需要修改、順序重要  |
| **Tuple** | ❌   | ✅   | ✅   | ✅   | 不可變、當 dict key |
| **Dict**  | ✅   | ✅\* | ❌   | Key  | Key-Value 映射      |
| **Set**   | ✅   | ❌   | ❌   | ❌   | 去重、集合運算      |

\*Python 3.7+ Dict 保證插入順序

---

## 🎓 面試常用技巧

### 1. 快速建立資料結構

```python
# 初始化
zeros = [0] * 10
matrix = [[0] * 3 for _ in range(3)]  # 3x3 矩陣

# Counter (計數神器)
from collections import Counter
cnt = Counter([1, 1, 2, 3, 3, 3])
# Counter({3: 3, 1: 2, 2: 1})
cnt.most_common(2)  # 最常見的2個
```

### 2. 型別轉換

```python
list("abc")      # ['a', 'b', 'c']
set([1, 2, 2])   # {1, 2}
dict([('a', 1), ('b', 2)])  # {'a': 1, 'b': 2}
tuple([1, 2, 3]) # (1, 2, 3)
```

### 3. 檢查空值

```python
if not lst:      # 空 list
if not d:        # 空 dict
if lst:          # 非空
```

### 4. 複製 vs 參考

```python
# 淺複製
lst2 = lst.copy()
lst2 = lst[:]
lst2 = list(lst)

# 深複製
from copy import deepcopy
lst2 = deepcopy(lst)
```

---

## ⚡ 時間複雜度速查

### List

- 索引 `lst[i]`: O(1)
- 搜尋 `x in lst`: O(n)
- append: O(1)
- insert: O(n)
- pop(): O(1)
- pop(0): O(n)

### Dict

- 取值 `d[key]`: O(1)
- 新增/刪除: O(1)
- `key in d`: O(1)

### Set

- 新增/刪除: O(1)
- `x in s`: O(1)
- 聯集/交集: O(len(s) + len(t))

---

## 💡 救命口訣

**選擇資料結構:**

1. 需要順序且常修改 → **List**
2. 需要順序但不修改 → **Tuple**
3. 需要快速查找配對 → **Dict**
4. 需要去重或集合運算 → **Set**

**面試卡住時:**

- 需要計數 → `Counter` 或 `defaultdict(int)`
- 需要去重 → `Set`
- 需要排序 → `sorted()` 或 `list.sort()`
- 兩個陣列對比 → 轉成 `Set` 做交集/差集
