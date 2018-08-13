class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        wordlist = [i.lower().strip("!?',;.") for i in paragraph.split()]
        counter = collections.Counter(wordlist)
        for b in banned:
            if b in counter:
                del counter[b]
        return counter.most_common(1)[0][0]
        