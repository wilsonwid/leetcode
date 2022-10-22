class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ls = []

        for ast in asteroids:
            while ls and ast < 0 < ls[-1]:
                if ls[-1] > abs(ast):
                    break
                elif ls[-1] < abs(ast):
                    ls.pop()
                    continue
                else:
                    ls.pop()
                break
            else:
                ls.append(ast)
        return ls
