class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        sorted_asteroids = sorted(asteroids)
        curr_mass = mass
        for m in sorted_asteroids:
            if curr_mass >= m:
                curr_mass += m
            else:
                return False
        return True