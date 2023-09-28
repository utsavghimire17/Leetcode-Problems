class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.right = Node(0,0)
        self.left = Node(0,0)
        self.right.prev = self.left
        self.left.next = self.right
    
    def insert(self,node): #at right
        prev = self.right.prev
        prev.next = node
        self.right.prev = node
        node.next = self.right
        node.prev = prev
        
    def remove(self,node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev
        
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        new_node = Node(key,value)
        self.insert(new_node)
        self.cache[key] = new_node
        print(len(self.cache))
        if len(self.cache) > self.capacity:
            least = self.left.next
            self.remove(least)
            del self.cache[least.key]
        
        
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)