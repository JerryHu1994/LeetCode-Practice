class Solution(object):
    def canTransform(self, start, end):
        """
        :type start: str
        :type end: str
        :rtype: bool
        """
        if start.count("R") != end.count("R") or start.count("L") != end.count("L") or start.count("X") != end.count("X"):
            return False
        ptr1, ptr2 = 0, 0
        while ptr1 < len(start) or ptr2 < len(end):
            while ptr1 < len(start) and start[ptr1] == "X":    ptr1 += 1
            while ptr2 < len(end) and end[ptr2] == "X":  ptr2 += 1
            if ptr1 == len(start) or ptr2 == len(end):  break
            if start[ptr1] != end[ptr2]:    return False
            if start[ptr1] == "R":
                if ptr1 > ptr2:
                    return False
            else:
                if ptr1 < ptr2:
                    return False
            ptr1 += 1
            ptr2 += 1
            print ptr1, ptr2
        return True