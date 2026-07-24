class LRUCache:

    def __init__(self, capacity: int):
        self.max_capacity = capacity
        self.cache_registry = OrderedDict()


    def get(self, key: int) -> int:

        if key not in self.cache_registry:
            return -1
        
        self.cache_registry.move_to_end(key)
        return self.cache_registry[key]


    def put(self, key: int, value: int) -> None:

        if key in self.cache_registry:
            self.cache_registry.move_to_end(key)
        
        self.cache_registry[key] = value

        if len(self.cache_registry) > self.max_capacity:
            self.cache_registry.popitem(last = False) 


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)