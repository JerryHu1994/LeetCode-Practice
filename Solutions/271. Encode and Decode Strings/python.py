class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        ret = ""
        for s in strs:  ret += str(len(s))+"#"+s
        return ret

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        ret = []
        while len(s):
            curr = 0
            while s[curr] != "#":
                curr += 1
            l = int(s[:curr])
            word = s[curr+1:curr+1+l]
            ret.append(word)
            s = s[curr+1+l:]
        return ret

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))