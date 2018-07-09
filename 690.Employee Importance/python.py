"""
# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        dic = {}
        for i in employees:
            dic[i.id] = (i.importance, i.subordinates)
        li, ret = [id], 0
        while len(li):
            curr = li.pop()
            ret += dic[curr][0]
            subs = dic[curr][1]
            for j in subs:
                li.append(j)
        return ret