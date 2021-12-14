class Solution:
    def reorderSpaces(self, text: str) -> str:
        wordlist = text.split()
        space_count = 0
        for val in text:
            if val == ' ':  space_count += 1
        if len(wordlist) == 0:
            return text
        if len(wordlist) == 1:
            return wordlist[0] + " "*space_count
        div = space_count//(len(wordlist)-1)
        remain = space_count%(len(wordlist)-1)
        mid = " "*div
        return mid.join(wordlist) + " "*remain