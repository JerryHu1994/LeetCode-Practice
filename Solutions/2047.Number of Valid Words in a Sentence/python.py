class Solution:
    def countValidWords(self, sentence: str) -> int:
        wordlist = sentence.split()
        ans = 0
        def isvalid(wordstr):
            has_hyphen = False
            for ind, char in enumerate(wordstr):
                if char.isdigit():
                    return False
                if char == '-':
                    if has_hyphen:  return False
                    has_hyphen = True
                    if ind == 0 or ind == len(wordstr)-1:   return False
                    if not wordstr[ind-1].isalpha() or not wordstr[ind+1].isalpha():    return False
                elif char in set(['!', '.', ',']):
                    if ind != len(wordstr)-1:   return False
                elif not char.isalpha():
                    return False
            return True
        for w in wordlist:
            if isvalid(w):  ans += 1
        return ans
        