class Solution:
    def capitalizeTitle(self, title: str) -> str:
        wordlist = title.split()
        res = []
        for w in wordlist:
            if len(w) <= 2:
                res.append(w.lower())
            else:
                res.append(w[0].upper() + w[1:].lower())
        return " ".join(res)