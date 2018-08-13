class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        visit = collections.defaultdict(int)
        for i in cpdomains:
            num, addr = i.split(" ")
            domains = addr.split(".")
            for i in range(len(domains)):
                domain = ".".join(domains[i:])
                visit[domain] += int(num)
        ret = []
        for key, val in visit.iteritems():
            ret.append(str(val) + " " + key)
        return ret