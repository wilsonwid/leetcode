class Solution(object):
    def maxSubarraySumCircular(self, A):
        
        def kadane(gen):
            # Maximum non-empty subarray sum
            ans = cur = 0
            for x in gen:
                cur = x + max(cur, 0)
                ans = max(ans, cur)
            return ans
        
        S = sum(A)
        if len(A) == 1:
            return S
        
        ans1 = kadane(iter(A))
        ans2 = S + kadane(-A[i] for i in range(1, len(A)))
        ans3 = S + kadane(-A[i] for i in range(len(A) - 1))
        ans4 = max(A)
        if ans4 < 0:
            return ans4
        return max(ans1, ans2, ans3)
