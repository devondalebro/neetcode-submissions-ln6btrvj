class TimeMap:

    def __init__(self):
        self.timeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeMap:
            self.timeMap[key] = []
        self.timeMap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        print(self.timeMap)
        if key not in self.timeMap:
            return ""
        
        vals = self.timeMap[key]
        if timestamp < vals[0][1]:
            return ""
        l, r = 0, len(vals) - 1
        res = ""
        while l <= r:
            m = l + (r - l) // 2
            if vals[m][1] <= timestamp:
                res = vals[m][0]
                l = m + 1
            else:
                r = m - 1

        return res