class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        import heapq
        squared_nums = list(map(lambda x: x**2, nums))
        heapq.heapify(squared_nums)
        return [heapq.heappop(squared_nums) for x in range(len(nums))]

