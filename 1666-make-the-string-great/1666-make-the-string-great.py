# remove two adjacent characters in s that are the same letter, with the leftmost character as lowercase and the rightmost is uppercase.
# 1. iterate through s
# 2. add every char to stack.
# 3. if the last element in stack is the same as current character (lowercased), skip it and pop stack
# 4. continue iterating until we reach the end of s.

class Solution:
    def makeGood(self, s: str) -> str: # "Pp"
        stack = []

        for c in s:
            if stack:
                prev = stack[-1]
                if (prev != c and prev == c.lower()) or (prev != c and prev == c.upper()):
                    stack.pop()
                    continue
            stack.append(c)
            
        return "".join(stack)
        