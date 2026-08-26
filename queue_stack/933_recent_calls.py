from collections import deque

class RecentCounter:

    def __init__(self):
        self.time_slot = deque()

    def ping(self, t: int) -> int:
        check = t - 3000
        self.time_slot.append(t)

        while self.time_slot and self.time_slot[0] < check:
            self.time_slot.popleft()

        return len(self.time_slot)
