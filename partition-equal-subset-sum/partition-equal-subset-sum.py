class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        @lru_cache(maxsize=None)
        def partition(subsetsum, n):
            if subsetsum == 0:
                return True
            elif subsetsum < 0 or n == 0:
                return False
            else:
                return partition(subsetsum, n-1) or partition(subsetsum - nums[n], n-1)
        
        summation = sum(nums)
        if summation % 2 != 0:
            return False
        else:
            return partition(summation//2, len(nums) - 1)
