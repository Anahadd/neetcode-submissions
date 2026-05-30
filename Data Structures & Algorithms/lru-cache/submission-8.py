from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.hashmap:
            self.hashmap.move_to_end(key) 
            return self.hashmap[key]
        return -1 

    def put(self, key: int, value: int) -> None:
        
        if key in self.hashmap: 
            self.hashmap[key] = value 
            self.hashmap.move_to_end(key)
        else:
            if len(self.hashmap) == self.capacity: 
                self.hashmap.popitem(last=False)
            self.hashmap[key] = value 

 