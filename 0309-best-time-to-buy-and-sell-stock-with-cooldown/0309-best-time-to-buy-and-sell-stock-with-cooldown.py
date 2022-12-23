class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        notHold, notHold_cooldown, hold = 0, float('-inf'), float('-inf')
        for i in prices:
            hold, notHold, notHold_cooldown = max(hold, notHold - i), max(notHold, notHold_cooldown), hold+i
        return max(notHold, notHold_cooldown)