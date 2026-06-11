class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losses = [-1] * 100001

        for winner, loser in matches:
            if losses[winner] == -1:
                losses[winner] = 0
            if losses[loser] == -1:
                losses[loser] = 1
            else:
                losses[loser] += 1

        ans = [[], []]
        for i in range(100001):
            if losses[i] == 0:
                ans[0].append(i)
            if losses[i] == 1:
                ans[1].append(i)

        return ans      
