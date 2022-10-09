class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        listing = [0] * 26
        for task in tasks:
            listing[ord(task) - ord("A")] += 1
        listing.sort()

        freq_max = listing.pop()
        idle_time = (freq_max - 1)*n
        while listing and idle_time > 0:
            popped = listing.pop()
            idle_time -= min(freq_max - 1, popped)
        idle_time = max(0, idle_time)
        return idle_time + len(tasks)
