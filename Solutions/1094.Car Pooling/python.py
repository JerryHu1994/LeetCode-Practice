class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        car_stops = []
        for trip in trips:
            num_passenger, from_point, to_point = trip
            car_stops.append((from_point, num_passenger))
            car_stops.append((to_point, -num_passenger))
        car_stops.sort()
        curr_cnt = 0
        for point, delta in car_stops:
            curr_cnt += delta
            if curr_cnt > capacity: return False
        return True