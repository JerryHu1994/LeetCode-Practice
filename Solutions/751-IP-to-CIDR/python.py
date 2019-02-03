class Solution(object):
    def ipToInt(self, ip):
        ret = 0
        for ind, val in enumerate(ip.split('.')[::-1]):
            ret += int(val) << ind * 8
        return ret
    
    def intToIP(self, integer):
        ans = []
        for i in range(4):
            ans.append(str((integer >> i*8) & 255))
        return ".".join(ans[::-1])
    
    def countzeros(self, ip):
        ret = 0
        while ip:
            if ip & 1:  break
            ret += 1
            ip >>= 1
        return ret
            
    
    def ipToCIDR(self, ip, n):
        """
        :type ip: str
        :type n: int
        :rtype: List[str]
        """
        ret, ind, ip_num = [], 0, self.ipToInt(ip)
        while ind < n:
            curr_zeros = self.countzeros(ip_num+ind)
            while ind + (1 << curr_zeros) > n:
                curr_zeros -= 1
            ret.append(self.intToIP(ip_num+ind)+"/"+str(32-curr_zeros))
            ind += 1 << curr_zeros
        return ret