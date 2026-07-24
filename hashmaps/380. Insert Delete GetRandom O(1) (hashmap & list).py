class RandomizedSet:

    def __init__(self):
        self.data_list = []
        self.index_registry = {}
        

    def insert(self, val: int) -> bool:
        if val in self.index_registry:
            return False
        
        self.index_registry[val] = len(self.data_list)
        self.data_list.append(val)

        return True
         

    def remove(self, val: int) -> bool:
        if val not in self.index_registry:
            return False
        
        target_index = self.index_registry[val]
        last_element = self.data_list[-1]

        self.data_list[target_index] = last_element
        self.data_list.pop()

        del self.index_registry[val]
        return True
        

    def getRandom(self) -> int:
        return random.choice(self.data_list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()