class Solution(object):
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        stack, i = [], 0
        currele, currnum = None, None
        while i < len(formula):
            if formula[i] == "(":
                stack.append("(")
                i += 1
            elif formula[i] == ")":
                temps = []
                while True:
                    curr = stack.pop()
                    if curr == "(": break
                    temps.append(curr)
                # get the next digit and apply to ()
                i += 1
                start = i
                while i < len(formula) and formula[i].isdigit():    i+=1
                mul = 1 if i==start else int(formula[start:i])
                for t in temps: stack.append([t[0], t[1]*mul]) 
            else:
                start = i
                i += 1
                while i<len(formula) and formula[i].islower():  i+=1
                currele = formula[start:i]
                currnum = ""
                while i<len(formula) and formula[i].isdigit():
                    currnum += formula[i]
                    i+=1 
                currnum = int(currnum) if len(currnum) > 0 else 1
                stack.append([currele, currnum])
        # clean the stack
        ret = collections.defaultdict(int)
        for s in stack: ret[s[0]] += s[1]
        res = ""
        for k in sorted(ret.iterkeys()):
            if ret[k] > 1:
                res += (k+str(ret[k]))
            else:
                res += k
        return res