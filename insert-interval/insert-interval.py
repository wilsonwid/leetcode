class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        ls = []
        last = -1
        for interval in intervals:
            if (interval[0] <= newInterval[0] <= interval[1] or interval[0] <= newInterval[1] <= interval[1] or newInterval[0] <= interval[0] and newInterval[1] >= interval[1]) and last == -1:
                last = [min(interval[0], newInterval[0]), max(newInterval[1], interval[1])]
                ls.append(last)
            elif last == -1:
                ls.append(interval)
            else:
                if interval[1] <= last[1]:
                    print(ls)
                    continue
                elif interval[0] <= last[1] <= interval[1]:
                    ls[-1][-1] = interval[1]
                else:
                    ls.append(interval)
            print(ls)
        if last == -1:
            for i in range(len(ls) - 1):
                if ls[i][1] < newInterval[0] and ls[i+1][0] > newInterval[1]:
                    ls.insert(i+1, newInterval)
                    return ls
            if ls[0][0] > newInterval[1]:
                ls.insert(0, newInterval)
            else:
                ls.append(newInterval)
        return ls
