class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0
        for i in range(len(strs[0])):
            for j in range(0, len(strs) - 1):
                if ord(strs[j][i]) <= ord(strs[j + 1][i]):
                    continue
                else:
                    count += 1
                    break
        return count
