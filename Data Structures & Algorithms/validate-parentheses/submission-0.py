class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close = { ")" : "(",   "}" : "{",   "]" : "[" }
        for bracket in s:
            if bracket in close:
                if stack and stack[-1] == close[bracket]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(bracket)
        return True if not stack else False
        