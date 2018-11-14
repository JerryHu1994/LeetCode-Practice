class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        pres, succs = collections.defaultdict(set), collections.defaultdict(set)
        # construct the pres and succs mapping
        for w1, w2 in zip(words, words[1:]):
            for a, b in zip(w1, w2):
                if a != b:
                    succs[a].add(b)
                    pres[b].add(a)
                    break
        allchars = set("".join(words))
        roots = allchars - set(pres.keys()) # roots are char without a pre so that we can start from them
        ret = ''
        while len(roots):
            curr = roots.pop()
            ret += curr
            if curr in succs:
                currsucc = succs[curr]
                for n in currsucc:
                    # only one pres remained, we can put it into the roots
                    if len(pres[n]) == 1:
                        pres.pop(n)
                        roots.add(n)
                    else:
                        pres[n].remove(curr)
                succs.pop(curr)
        return ret if len(ret) == len(allchars) else ''