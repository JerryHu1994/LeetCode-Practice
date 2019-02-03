class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        self.dic = collections.defaultdict(list)
        for p in paths:
            splited = p.split()
            root_path = splited[0]
            for f in splited[1:]:
                filename, filecontent = f.replace("(", " ").replace(")", " ").split()
                self.dic[filecontent].append(root_path + "/" + filename)
        ret = []
        for v in self.dic.values():
            if len(v) > 1:
                ret.append(v)
        return ret 
                