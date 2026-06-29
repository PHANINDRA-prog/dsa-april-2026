from collections import defaultdict

class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.freq = 1

        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.size = 0
        self.head = Node(0,0)
        self.tail = Node(0,0)

        self.head.next = self.tail
        self.tail.prev = self.head
    
    def insert(self,node):
        prev = self.tail.prev
        prev.next = node
        node.prev = prev

        node.next = self.tail
        self.tail.prev = node

        self.size += 1
    
    def remove(self,node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

        self.size -= 1
    
    def removeLRU(self):
        if self.head.next == self.tail:
            return None
        
        node = self.head.next
        self.remove(node)
        return node
    

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self. minFreq = 0
        # First HashMap Key -> Node
        self.keyToNode = {}
        # Second Hashmap freq -> DLL
        self.freqToList = defaultdict(DoublyLinkedList)

    def get(self, key: int) -> int:
        # Key Not Found
        if key not in self.keyToNode:
            return -1
        
        node = self.keyToNode[key]
        self.freqToList[node.freq].remove(node)

        if (node.freq == self.minFreq and self.freqToList[node.freq].size == 0):
            self.minFreq += 1
        
        node.freq += 1
        self.freqToList[node.freq].insert(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        
        if key in self.keyToNode:
            node = self.keyToNode[key]
            node.value = value
            self.get(key)
            return
        
        if len(self.keyToNode) == self.capacity:
            dll = self.freqToList[self.minFreq]
            node = dll.removeLRU()
            del self.keyToNode[node.key]
        
        node = Node(key,value)
        self.keyToNode[key] = node
        self.freqToList[1].insert(node)
        self.minFreq = 1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)