class Solution:
    def memLeak(self, memory1: int, memory2: int) -> List[int]:
        time = 1
        while time <= memory1 or time <= memory2:
            if memory1 < memory2:
                memory2 -= time
            else:
                memory1 -= time
            time += 1
        return [time, memory1, memory2]