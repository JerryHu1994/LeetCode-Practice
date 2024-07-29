# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        hostname = startUrl[7:].split("/")[0]
        q = [startUrl]
        visited = set([startUrl])
        ans = []
        while len(q):
            nextq = []
            for curr_url in q:
                if curr_url[7:].split("/")[0] == hostname:
                    ans.append(curr_url)
                else:
                    continue
                next_urls = htmlParser.getUrls(curr_url)
                for next_url in next_urls:
                    if next_url not in visited:
                        nextq.append(next_url)
                        visited.add(next_url)
            q = nextq
        return ans