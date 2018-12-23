class Solution(object):
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        hex = "1234567890abcdefABCDEF"
        if IP.count(".") == 3:
            for each in IP.split("."):
                if not each.isdigit() or str(int(each)) != each or int(each) < 0 or int(each) > 255:
                    return "Neither"
            return "IPv4"
        
        if IP.count(":") == 7:
            for each in IP.split(":"):
                if not each or not each.isalnum() or len(each) > 4 or any(char not in hex for char in each):    return "Neither"
            return "IPv6"
        return "Neither"