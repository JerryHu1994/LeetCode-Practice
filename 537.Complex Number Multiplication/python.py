class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a_list, b_list = a.split("+"), b.split("+")
        a_real, b_real = int(a_list[0]), int(b_list[0])
        a_complex, b_complex = int(a_list[1][:-1]), int(b_list[1][:-1])
        ret_real = a_real*b_real - a_complex*b_complex
        ret_complex = a_real*b_complex + a_complex*b_real
        return str(ret_real)+"+"+str(ret_complex)+"i"