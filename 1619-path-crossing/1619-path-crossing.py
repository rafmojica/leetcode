class Solution:
    def isPathCrossing(self, path: str) -> bool:
        # (0, 0) --> origin
        # (0, 0 + 1) --> north
        # (0 + 1, 0) --> east
        # (0 - 1, 0) --> west
        # (0, 0 - 1) --> south
        
        curr = [[0, 0]]
        for p in path:
            lastPos = curr[-1][:]
            
            if p == 'N':
                lastPos[1] += 1
            elif p == 'E':
                lastPos[0] += 1
            elif p == 'W':
                lastPos[0] -= 1
            elif p == 'S':
                lastPos[1] -= 1

            if lastPos in curr:
                return True

            curr.append(lastPos)

        return False