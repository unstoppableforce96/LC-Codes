class MyHashMap:

    def __init__(self):
        self.map = []

    def put(self, key: int, value: int) -> None:
        for i in range(len(self.map)):
            if self.map[i][0] == key:
                self.map[i][1] = value
                break
        else:
            self.map.append([key, value])
    def get(self, key: int) -> int:
        for i in range(len(self.map)):
            if self.map[i][0] == key:
                return self.map[i][1]
        return -1

    def remove(self, key: int) -> None:
        remove_index = -1
        for i in range(len(self.map)):
            if self.map[i][0] == key:
                remove_index = i
        if remove_index != -1:
            self.map.pop(remove_index)

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)