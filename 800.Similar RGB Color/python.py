class Solution(object):
    def similarRGB(self, color):
        """
        :type color: str
        :rtype: str
        """
        hexlist = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
        colorlist = [color[1:3], color[3:5], color[5:7]]
        ret = "#"
        for c in colorlist:
            print c
            firstdigit = c[0]
            curr = c[0]+c[0]
            large = hexlist[hexlist.index(firstdigit)+1] if hexlist.index(firstdigit) != len(hexlist)-1 else hexlist[hexlist.index(firstdigit)]
            small = hexlist[hexlist.index(firstdigit)-1] if hexlist.index(firstdigit) != 0 else hexlist[hexlist.index(firstdigit)]
            large = large+large
            small = small+small
            smallint, largeint, currint, colorint = int(small, 16), int(large, 16), int(curr, 16), int(c, 16)
            diffs = [abs(smallint-colorint), abs(largeint-colorint), abs(currint-colorint)]
            if min(diffs) == abs(smallint-colorint):
                newhex = small
            if min(diffs) == abs(largeint-colorint):
                newhex = large
            if min(diffs) == abs(currint-colorint):
                newhex = curr
            ret += newhex
        return ret