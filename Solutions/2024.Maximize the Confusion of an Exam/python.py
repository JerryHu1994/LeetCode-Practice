class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        truecount, falsecount = 0, 0
        leftptr, rightptr = 0, 0
        l = len(answerKey)
        ans = 0
        while rightptr < l:
            while rightptr < l:
                if answerKey[rightptr] == 'T':
                    truecount += 1
                else:
                    falsecount += 1
                rightptr += 1
                if min(truecount,falsecount) <= k:
                    ans = max(ans, rightptr - leftptr)
                else:
                    break
            if rightptr >= l:   break
            while True:
                if answerKey[leftptr] == 'T':
                    truecount -= 1
                else:
                    falsecount -= 1
                leftptr += 1
                if min(truecount,falsecount) <= k:
                    break
        return ans