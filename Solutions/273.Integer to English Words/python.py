class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:    return "Zero"
        def helper(num):
            nums = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve",
                   "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
            tens = ["Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
            dic = [(1000000000,"Billion"), (1000000,"Million"), (1000,"Thousand"), (100,"Hundred")]
            for p in dic:
                div, name = p
                if num >= div:
                    first, second = num/div, num%div
                    ret = [helper(first), name]
                    if second != 0: ret.append(helper(second))
                    return " ".join(ret)
            if num < 20:
                return nums[num-1]
            else:
                first, second = num/10, num%10
                return tens[first-2] if second == 0 else tens[first-2]+" "+nums[second-1]
        return helper(num)