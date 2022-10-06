from sortedcontainers import SortedDict

class TimeMap:

    def __init__(self):
        self.d = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:

        if not key in self.d : self.d[key] = SortedDict()
        self.d[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.d: return ""

        it = self.d[key].bisect_right(timestamp)

        return "" if it == 0 else self.d[key].peekitem(it - 1)[1]








        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)