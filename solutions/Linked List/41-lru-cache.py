// TC : O(n)
// SC : O(n)
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = []

    def get(self, key: int) -> int:
        # Front is the least used element and Back is the most recently used element
        # Traverse through the array to find the element
        # Next step is to remove the value at that index
        # And add the key value pair at the end of the array

        for i in range(len(self.cache)):
            k,v = self.cache[i]

            if k == key:
                self.cache.pop(i)
                self.cache.append((k,v))
                return v
        return -1

    def put(self, key: int, value: int) -> None:
        # Front is the least used element and Back is the most recently used element
        # If The value is present and we have a new value for that key pair then delete the old entry and then add the new entry at the end
        # Now in the case key value pair is new and  then size is capacity what to do is remove the front of the array
        # Then add the value at the end

        for i in range(len(self.cache)):
            k,v = self.cache[i]

            if k == key:
                self.cache.pop(i)
                self.cache.append((key,value))
                return
        if len(self.cache) == self.capacity:
            self.cache.pop(0)
        self.cache.append((key,value))





# Optimized Approach

class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.head = Node(0,0)
        self.tail = Node(0,0)

        self.head.next = self.tail
        self.tail.prev = self.head
    
    def remove(self,node):
        previous = node.prev
        nxt = node.next
        
        previous.next = nxt
        nxt.prev = previous
    
    def insert(self,node):
        previous = self.tail.prev

        previous.next = node
        node.prev = previous

        node.next = self.tail
        self.tail.prev = node
    
    def get(self,key):
        if key not in self.cache:
            return -1
        
        node = self.cache[key]

        self.remove(node)
        self.insert(node)

        return node.value
    
    def put(self,key,value):
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            node.value = value
            self.insert(node)
            return
        
        node = Node(key,value)

        self.cache[key] = node
        self.insert(node)

        if len(self.cache) > self.capacity:
            lru = self.head.next
            self.remove(lru)
            del self.cache[lru.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)