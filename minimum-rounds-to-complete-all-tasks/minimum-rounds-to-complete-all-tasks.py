class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        d = {}
        for task in tasks:
            d[task] = d.get(task, 0) + 1
        
        minrounds = 0
        for task in d.keys():
            if d[task] == 1:
                return -1
            if d[task] % 3 == 0:
                minrounds += d[task] // 3
            else:
                minrounds += (d[task] // 3) + 1
        return minrounds
