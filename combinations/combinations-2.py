class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        output = []
        def recurse(first = 1, cur = []):
            if len(cur) == k:
                output.append(cur[:])
            for i in range(first, n + 1):
                cur.append(i)
                recurse(i+1, cur)
                cur.pop()
        recurse()
        return output
