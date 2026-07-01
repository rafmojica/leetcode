class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = {")": "(", "}": "{", "]": "["}

        for p in s:
            if p in pair and len(stack) > 0 and pair[p] == stack[-1]:
                stack.pop()
            else:
                stack.append(p)

        return not stack
