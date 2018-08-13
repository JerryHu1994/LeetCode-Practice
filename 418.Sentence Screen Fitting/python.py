class Solution(object):
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        sen = " ".join(sentence) + " "
        curr, l = 0, len(sen)
        for r in range(rows):
            curr += cols
            if sen[curr%l] == " ":
                curr += 1
            else:
                while curr > 0 and sen[(curr-1)%l] != " ":
                    curr -= 1 
        return curr / l