class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        s = set()
        for c in sentence:
            s.add(c)
        if s == set(string.ascii_lowercase):
            return True
        else:
            return False

