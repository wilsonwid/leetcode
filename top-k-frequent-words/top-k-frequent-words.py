import heapq
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d = {}
        return_ls = []
        for word in words:
            d[word] = d.get(word, 0) + 1
        ls = list(sorted([(-x[1], x[0]) for x in d.items()], key = lambda x: x[1]))
        heapq.heapify(ls)
        i = 0
        while ls and i < k:
            return_ls.append(ls[0][1])
            heapq.heappop(ls)
            i += 1
        return return_ls
            
