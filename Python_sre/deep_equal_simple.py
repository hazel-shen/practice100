def deepEqual_simple(obj1, obj2):
    if type(obj1) != type(obj2):
        return False
    
    # primitive type comparison
    if isinstance(obj1, (int, float, str, bool)) or obj1 is None:
        return obj1 == obj2
    
    # deal with dictionary
    if isinstance(obj1, dict):
        if obj1.keys() != obj2.keys():
            return False
        
        for key in obj1:
            if not deepEqual_simple(obj1[key], obj2[key]):
                return False
        
        return True
    
    # deal with list
    if isinstance(obj1, list):
        if len(obj1) != len(obj2):
            return False
        
        for i in range(len(obj1)):
            if not deepEqual_simple(obj1[i], obj2[i]):
                return False
        
        return True




print(deepEqual_simple({"a":1,"b":[2]}, {"b":[2],"a":1}))  # True
print(deepEqual_simple([1,2,[3]], [1,2,[3]]))             # True
print(deepEqual_simple({"a":1}, {"a":"1"}))               # False
print(deepEqual_simple({"a":1}, {"a":1,"b":2}))           # False
print(deepEqual_simple([1,2], [1,2,3]))                   # False