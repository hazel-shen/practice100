# head <--> node <--> node <--> tail
# hashmap & list
# get and put in O(1)
import threading
class Node:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
        
class DoublyLinkedList:
    def __init__(self):
        self.head = Node() # dummy
        self.tail = Node() # dummy
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def add_to_front(self, node):
        # head <-> old_first
        # head <-> node <-> old_first
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def remove(self, node):
        # remove specific node, O(1)
        node.prev.next = node.next
        node.next.prev = node.prev

    def remove_last(self):
        # remove the last node (which is not used recently), O(1)
        if self.tail.prev is self.head:
            return None
        last = self.tail.prev
        self.remove(last)
        return last
    
    def debug_print(self):
        cur = self.head.next
        vals = []
        while cur is not self.tail:
            vals.append(f"({cur.key},{cur.val})")
            cur = cur.next
        print(" -> ".join(vals))

class LRUCache(object):
    def __init__(self, capacity):
        self.cap = capacity
        self.map = {}
        self.list = DoublyLinkedList()
        # Initialize a Mutex Lock
        self.lock = threading.Lock()

    def get(self, key):
        with self.lock:
            if key not in self.map:
                return -1
            node = self.map[key]
            self.list.remove(node)
            self.list.add_to_front(node)
            return node.val        

    def put(self, key, value):
        # key exists, remove that node at first
        with self.lock:
            if key in self.map:
                old = self.map[key]
                self.list.remove(old)

            # And create a new Node, add it to the front of the list
            node = Node(key, value)
            self.list.add_to_front(node)
            self.map[key] = node

            # If excess the capacity, drop the last one out
            if len(self.map) > self.cap:
                last = self.list.remove_last()
                del self.map[last.key]


    def put_if_absent(self, key, value):
        with self.lock:
            node = Node(key, value)
            if key not in self.map:
                self.list.add_to_front(node)
                self.map[key] = node
                
            # If excess the capacity, drop the last one out
            if len(self.map) > self.cap:
                last = self.list.remove_last()
                if last: # Prevent from the last pair is null
                    del self.map[last.key]
    


    def delete(self, key):
        # Delete specific key
        with self.lock:
            if key in self.map:
                old = self.map[key]
                self.list.remove(old)
                del self.map[key]

    def peek(self, key):
        # get the value depends on what key is
        with self.lock:
            if key not in self.map:
                return -1
            return self.map[key].val
    
    def resize(self, new_size):
        # when cale in the size, evict extra nodes.
        with self.lock:
            while len(self.map) > new_size:
                last = self.list.remove_last()
                del self.map[last.key]
            self.cap = new_size

cache = LRUCache(5)
cache.put(1, 10)
cache.list.debug_print()   # Check up on the list
cache.put(2, 20)
cache.list.debug_print()
cache.put(3, 30)
cache.put(5, 50)
cache.list.debug_print()
cache.resize(3)
cache.list.debug_print()
cache.delete(3)
cache.list.debug_print()
cache.put_if_absent(2, 20)
cache.list.debug_print()
print(cache.peek(1))

