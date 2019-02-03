class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False
        if A == B:
            # equal case
            if len(A) == len(set(A)):
                return False
            else:
                return True
        else:
            # not equal case
            lista, listb = [], []
            for i in range(len(A)):
                if A[i] != B[i]:
                    lista.append(A[i])
                    listb.append(B[i])   
            if len(lista) != 2:
                return False
            else:
                if lista[0] == listb[1] and lista[1] == listb[0]:
                    return True
                else:
                    return False