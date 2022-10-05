import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        new_stone = [-x for x in stones]
        heapq.heapify(new_stone)
        while new_stone:
            a = new_stone[0]
            heapq.heappop(new_stone)
            if not new_stone:
                return -a
            b = new_stone[0]
            heapq.heappop(new_stone)
            print(new_stone)
            heapq.heappush(new_stone, -abs(a - b))
