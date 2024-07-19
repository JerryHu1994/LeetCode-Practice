class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        sorted_prices = sorted(prices)
        sum_of_cho = sum(sorted_prices[:2])
        if sum_of_cho <= money:
            return money - sum_of_cho
        else:
            return money