class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        d = {}
        max_num = 0

        for num in nums:
            d[num] = d.get(num, 0) + num
            max_num = max(max_num, num)
        
        @cache
        def maximiser(num):
            if num == 0:
                return 0
            if num == 1:
                return d.get(1, 0)
            return max(maximiser(num-1), maximiser(num-2) + d.get(num, 0))
        return maximiser(max_num)
