class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        if not words:
            return 0
        d = {}
        length = 0
        flag = False
        for word in words:
            palin = word[::-1]
            if palin in d and d[palin] != 0:
                length += 4
                d[palin] = d[palin] - 1
                if d[palin] == 0:
                    del d[palin]
            else:
                d[word] = d.get(word, 0) + 1
        for key in d.keys():
            if key == key[::-1]:
                flag = True
                break
        if flag:
            return length + 2
        else:
            return length
