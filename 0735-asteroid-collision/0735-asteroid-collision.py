class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # 1. initialize a stack
        # 2. push every asteroid in stack.
        #   - push from left to right
        #   - if stack[-1] is positive, and we encounter an asteroid that is negative, one of the two will happen:
        #       1. if bigger than stack[-1], continuously pop stack.
        #       2. if smaller than stack[-1], skip.

        stack = []

        # [4, 2, -1, -2, 12, -13] --> [-13]
        # [3, 5, -6, -7] --> [-6, -7]
        # [-1, 1, 1, 2] --> [-1, 1, 1, 2]

        for asteroid in asteroids:
            while stack and stack[-1] > 0 and asteroid < 0:
                if abs(asteroid) > stack[-1]:
                    stack.pop() # remove smaller asteroid going right
                else:
                    break

            if stack and asteroid < 0:
                if abs(asteroid) < stack[-1]:
                    continue
                if abs(asteroid) == stack[-1]:
                    stack.pop()
                    continue
            
            stack.append(asteroid)
        
        return stack
