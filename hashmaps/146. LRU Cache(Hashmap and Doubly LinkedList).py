class Node:
    def __init__(self, key:int, value:int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def _remove_node(self, target_node:Node) -> None:
        previous_neighbour = target_node.prev
        next_neighbour = target_node.next

        previous_neighbour.next = next_neighbour
        next_neighbour.prev = previous_neighbour

    def _add_to_most_recent(self, target_node:Node) -> None:
        current_most_recent = self.most_recently_used.prev
        
        current_most_recent.next = target_node
        target_node.prev = current_most_recent

        target_node.next = self.most_recently_used
        self.most_recently_used.prev = target_node

    def __init__(self, capacity: int):
        self.max_capacity = capacity
        self.cache_registry = {}

        self.least_recently_used = Node(0, 0)
        self.most_recently_used = Node(0, 0)

        self.least_recently_used.next = self.most_recently_used
        self.most_recently_used.prev = self.least_recently_used
       

    def get(self, key: int) -> int:
        if key in self.cache_registry:
            accessed_node = self.cache_registry[key]
            self._remove_node(accessed_node)
            self._add_to_most_recent(accessed_node)
            return accessed_node.value
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache_registry:
            existing_node = self.cache_registry[key]
            self._remove_node(existing_node)
            del self.cache_registry[key]

        new_node = Node(key, value)
        self.cache_registry[key] = new_node
        self._add_to_most_recent(new_node)

        if len(self.cache_registry) > self.max_capacity:
            oldest_node = self.least_recently_used.next
            self._remove_node(oldest_node)
            del self.cache_registry[oldest_node.key]
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)