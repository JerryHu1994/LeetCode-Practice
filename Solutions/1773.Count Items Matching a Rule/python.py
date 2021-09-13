class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        dic = {"type": 0, "color":1, "name": 2}
        return [li[dic[ruleKey]] for li in items].count(ruleValue)