class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        sub_dic = {4: "IV", 9:"IX", 40:"XL", 90:"XC", 400:"CD", 900:"CM"}
        dic = {1:"I", 5:"V", 10:"X", 50:"L", 100:"C", 500:"D", 1000:"M"}
        div = 10
        ret = ""
        while num != 0:
            remainfull = num%div
            unit = div/10
            remain = remainfull/unit
            if remainfull in sub_dic:
                ret = sub_dic[remainfull] + ret
            else:
                if remain < 5:
                    ret = dic[unit]*remain + ret
                else:
                    ret = dic[5*unit] + dic[unit]*(remain-5) + ret
            num -= remainfull
            div *= 10
        return ret