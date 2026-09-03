class Solution:
    def removeStars(self, s: str) -> str:
        # iterate through each character in s, append each char to a stack
        # for every * encountered, skip and pop the top of stack. 
        # continue until we reach the end of s, and return stack.join("").
        stack = []

        for c in s:
            if stack and c == '*':
                stack.pop()
            else:
                stack.append(c)
        
        return "".join(stack)
