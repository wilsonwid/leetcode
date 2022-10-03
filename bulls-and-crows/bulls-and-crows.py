class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        d1 = {}
        d2 = {}
        for i in range(len(secret)):
            d1[i] = secret[i]
            d2[secret[i]] = d2.get(secret[i], 0) + 1
        a = 0
        b = 0
        for i in range(len(guess)):
            if (i in d1 and d1[i] == guess[i]):
                a += 1
                del d1[i]
                d2[guess[i]] = d2[guess[i]] - 1
                if (d2[guess[i]] == 0):
                    del d2[guess[i]]
        for i in range(len(guess)):
            if (i in d1 and guess[i] in d2):
                b += 1
                d2[guess[i]] = d2[guess[i]] - 1
                if d2[guess[i]] == 0:
                    del d2[guess[i]]
        return f"{a}A{b}B"
