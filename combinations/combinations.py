class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        def recurse(ls, possible):
            if len(ls) == k:
                return [ls]
            elif not possible:
                return []
            else:
                return recurse(ls + [possible[0]], possible[1:]) + recurse(ls, possible[1:])
        return recurse([], list(range(1, n+1)))
