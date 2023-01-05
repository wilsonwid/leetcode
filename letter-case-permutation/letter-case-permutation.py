class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        output = []

        def recurse(cur, remaining):
            if len(remaining) == 0:
                output.append(cur[:])
            elif remaining[0].isalpha():
                recurse(cur + [remaining[0].lower()], remaining[1:])
                recurse(cur + [remaining[0].upper()], remaining[1:])
            else:
                recurse(cur + [remaining[0]], remaining[1:])
        recurse([], [x for x in s])
        return list(["".join(x) for x  in output])
