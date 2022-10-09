class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        listing = [0] * 26
        for task in tasks:
            listing[ord(task) - ord("A")] += 1
        f_max = max(listing)
        count = listing.count(f_max)
        return max((f_max - 1)*(n+1) + count, len(tasks))
