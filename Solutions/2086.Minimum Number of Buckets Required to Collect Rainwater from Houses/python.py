class Solution:
    def minimumBuckets(self, street: str) -> int:
        if len(street) == 0:
            return 0
        l = len(street)
        i = 0
        s = set()
        while i < len(street):
            if street[i] == "H":
                if (i == 0 or street[i-1] == "H") and (i == l-1 or street[i+1] == "H"):
                    return -1
                if i-1 not in s:
                    if i == l-1 or street[i+1] == "H":
                        s.add(i-1)
                    else:
                        s.add(i+1)
            i += 1
        return len(s)
            