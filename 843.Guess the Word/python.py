# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Master(object):
#    def guess(self, word):
#        """
#        :type word: str
#        :rtype int
#        """

class Solution(object):
    def findSecretWord(self, wordlist, master):
        """
        :type wordlist: List[Str]
        :type master: Master
        :rtype: None
        """
        def match(a, b):
            ans = 0
            for i in range(len(a)):
                if a[i] == b[i]:    ans += 1
            return ans
        n = 0
        while n < 6:
            count = collections.Counter(w1 for w1, w2 in itertools.permutations(wordlist, 2) if match(w1, w2) == 0)
            guess_word = min(wordlist, key=lambda w: count[w])
            n = master.guess(guess_word)
            wordlist = [w for w in wordlist if match(w, guess_word) == n]
            