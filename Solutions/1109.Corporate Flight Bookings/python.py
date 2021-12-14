class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        ans = [0]*(n+2)
        for start, end, seats in bookings:
            ans[start] += seats
            ans[end+1] -= seats
        for ind in range(2, n+1):
            ans[ind] = ans[ind-1]+ans[ind]
        return ans[1:-1]