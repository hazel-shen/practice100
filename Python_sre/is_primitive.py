def is_primitive(obj):
    return isinstance(obj, (int, str, float, bool)) or obj is None

assert is_primitive(1)
assert is_primitive("a")
assert is_primitive(None)
assert not is_primitive([1,2])

print("All tests passed!")