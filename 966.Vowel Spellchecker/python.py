class Solution(object):
    def spellchecker(self, wordlist, queries):
        """
        :type wordlist: List[str]
        :type queries: List[str]
        :rtype: List[str]
        """
        vowel = lambda w : "".join("*" if c in 'aeiou' else c for c in w)
        word_set = set(wordlist)
        words_cap = {}
        words_vow = {}
        for w in wordlist:
            if w.lower() not in words_cap:
                words_cap[w.lower()] = w
            if vowel(w.lower()) not in words_vow:
                words_vow[vowel(w.lower())] = w
        ans = []
        def helper(query):
            if query in word_set:   return query
            query_low = query.lower()
            if query_low in words_cap:
                return words_cap[query_low]
            voweled = vowel(query_low)
            if voweled in words_vow:
                return words_vow[voweled]
            return ""
        for q in queries:
            ans.append(helper(q))
        return ans