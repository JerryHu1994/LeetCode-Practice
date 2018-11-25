class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        split_emails = [e.split("@")    for e in emails]
        email_set = set()
        for e in split_emails:
            local = ""
            for char in e[0]:
                if char == "+": break
                if char == ".": continue
                local += char
            email_set.add(local+"@"+e[1])
        return len(email_set)