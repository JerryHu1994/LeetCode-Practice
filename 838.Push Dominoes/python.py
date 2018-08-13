class Solution(object):
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        domi_list = [None]*len(dominoes)
        # sweep from left right
        currright = None
        for i in range(len(dominoes)):
            if dominoes[i] == "R":
                domi_list[i] = ["R", 0]
                currright = i
            elif dominoes[i] == "L":
                currright = None
            else:
                if currright != None:   domi_list[i] = ["R", i - currright]
        # sweep from right to left
        currleft = None
        for i in range(len(dominoes)-1, -1, -1):
            if dominoes[i] == "L":
                domi_list[i] = ["L", 0]
                currleft = i
            elif dominoes[i] == "R":
                currleft = None
                continue
            else:
                if currleft != None:
                    if domi_list[i] == None:
                        domi_list[i] = ["L", currleft - i]
                    else:
                        if domi_list[i][1] > currleft - i:
                            domi_list[i] = ["L", currleft - i]
                        elif domi_list[i][1] == currleft - i:
                            domi_list[i] = None
        ret = ""
        for i in domi_list:
            if i == None:
                ret += "."
            elif i[0] == "L":
                ret += "L"
            else:
                ret += "R"
        return ret
                
                
                
            