class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        ret = set()
        for e in emails:
            local, domain = e.split("@")
            reallocal = ""
            for i in local:
                if i == "+":
                    break
                elif i == ".":
                    continue
                reallocal += i
            full = reallocal+"@"+domain
            ret.add(full)
        return len(ret)