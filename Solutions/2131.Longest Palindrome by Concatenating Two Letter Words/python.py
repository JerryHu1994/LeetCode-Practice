class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        dic = defaultdict(int)
        for word in words:
            dic[word] += 1
        ans = 0
        wordlist = [w for w in dic]
        for word in wordlist:
            reverseword = word[::-1]
            if word[0] == word[1]:
                count = dic[word]//2
                ans += count*4
                dic[word] -= count*2
                if dic[word] == 0:  del dic[word]
            else:
                if reverseword in dic:
                    mincount = min(dic[word], dic[reverseword])
                    dic[word] -= mincount
                    dic[reverseword] -= mincount
                    if dic[word] == 0:  del dic[word]
                    if dic[reverseword] == 0:  del dic[reverseword]
                    ans += mincount*4
        for word in dic:
            if word[0] == word[1]:
                ans += 2
                break
        return ans