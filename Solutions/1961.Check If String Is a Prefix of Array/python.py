class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        for i in range(len(words)):
            if ''.join(words[:i+1])==s: return True
        return False