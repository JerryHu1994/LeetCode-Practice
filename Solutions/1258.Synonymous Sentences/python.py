class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        word_dic = defaultdict(list)
        for s, t in synonyms:
            word_dic[s].append(t)
            word_dic[t].append(s)
        word_list = text.split()
        @lru_cache()
        def bfs(word):
            queue = [word]
            ans = []
            visited = set([word])
            while len(queue):
                currword = queue.pop(0)
                ans.append(currword)
                nextlist = word_dic[currword]
                for nextword in nextlist:
                    if nextword not in visited:
                        queue.append(nextword)
                        visited.add(nextword)
            return sorted(ans)
        self.ans = []
        def backtrack(pre_sentence, ind):
            if ind == len(word_list):
                self.ans.append(pre_sentence)
                return
            word = word_list[ind]
            syn_words = bfs(word) if word in word_dic else [word]
            for syn in syn_words:
                nextsentence = pre_sentence + syn if ind == 0 else pre_sentence + " " + syn
                backtrack(nextsentence, ind+1)
        backtrack("", 0)
        return self.ans