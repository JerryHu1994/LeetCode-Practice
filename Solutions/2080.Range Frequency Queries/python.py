class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.count = defaultdict(list)
        for ind, val in enumerate(arr):
            self.count[val].append(ind)

    def query(self, left: int, right: int, value: int) -> int:
        first = bisect.bisect(self.count[value], left-1)
        second = bisect.bisect(self.count[value], right)
        return second - first

# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)