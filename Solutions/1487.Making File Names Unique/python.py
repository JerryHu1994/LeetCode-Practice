class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        assigned_set = set()
        mem_dic = {}
        ans = []
        for name_to_create in names:
            curridx = 0 if name_to_create not in mem_dic else mem_dic[name_to_create]
            name_to_create_add = name_to_create if curridx == 0 else name_to_create + "("+str(curridx)+")"
            while name_to_create_add in assigned_set:
                curridx += 1
                name_to_create_add = name_to_create + "("+str(curridx)+")"
            ans.append(name_to_create_add)
            assigned_set.add(name_to_create_add)
            mem_dic[name_to_create] = curridx + 1
        return ans