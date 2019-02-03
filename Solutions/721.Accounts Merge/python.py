class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        dic = collections.defaultdict(list)
        # email -> a list of index
        for ind, entry in enumerate(accounts):
            for email in entry[1:]:
                dic[email].append(ind)
        visited = [False]*len(accounts)
        ret = []
        for i in range(len(accounts)):
            if visited[i]:  continue
            root = accounts[i][1] # grab the first email
            queue = [i]
            emailset = set()
            while len(queue):
                curr = queue.pop(0) # current index of account
                visited[curr] = True
                for j in accounts[curr][1:]:
                    if j not in emailset:   emailset.add(j)
                    for index in dic[j]:# add unvisited indexes to the queue
                        if visited[index]:  continue
                        queue.append(index)
            currlist = [accounts[i][0]] + sorted(list(emailset))
            ret.append(currlist)
        return ret
                    
        