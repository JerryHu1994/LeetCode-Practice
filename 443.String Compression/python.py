class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        left, curr, ind = 0, 1, 1
        while ind < len(chars)+1:
            if ind < len(chars) and chars[left] == chars[ind]:
                curr+=1
                del chars[ind]
            else:
                if curr != 1:
                    numlist = [i for i in str(curr)]
                    for j in numlist:
                        chars.insert(ind, j)
                        ind += 1
                    left = ind
                else:
                    left = ind
                ind = left+1
                curr = 1
        return len(chars)
        
            