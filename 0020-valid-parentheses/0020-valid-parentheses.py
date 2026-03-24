class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parenthesis = {")" : "(", "]" : "[", "}": "{"}
        for c in s:
            if c in parenthesis:
                if stack and stack[-1] == parenthesis[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        if not stack:
            return True    
        return False