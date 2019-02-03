class Solution(object):
    
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        carry, i, j = 0, len(a)-1, len(b)-1
        ret = ""
        while i>=0 or j>=0:
            aval, bval = 0, 0
            if i>=0:
                if int(a[i]):
                    aval = 1
            if j>=0:
                if int(b[j]):
                    bval = 1
            s = carry + aval + bval
            carry, curr = s/2, s%2
            ret = str(curr) + ret
            i-=1
            j-=1
        if carry:   ret = "1" + ret 
        return ret
        