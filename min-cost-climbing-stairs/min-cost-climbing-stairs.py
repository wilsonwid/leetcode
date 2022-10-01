class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        lst = [0 for x in range(len(cost))]
        lst[1] = cost[1]
        lst[0] = cost[0]
        for i in range(len(cost)):
            if i-1 >= 0 and i-2>=0:
                lst[i] = min(lst[i-1], lst[i-2]) + cost[i]
        return min(lst[-1], lst[-2])
