class Solution(object):
    def paintWalls(self, cost, time):
        n = len(cost)
        money = [float('inf')] * (n + 1)
        money[0] = 0
        for i in range(n):
            for j in range(n, 0, -1):
                money[j] = min(money[j], money[max(j - time[i] - 1, 0)] + cost[i])
        return money[n]