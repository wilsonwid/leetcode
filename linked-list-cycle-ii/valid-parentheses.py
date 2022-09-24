class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {"}": "{", "]": "[", ")": "("}
        
        for char in s:
            if char in mapping:
                popped = stack.pop() if stack else "."
                if (popped != mapping[char]):
                    return False
            else:
                stack.append(char)
        return not stack
