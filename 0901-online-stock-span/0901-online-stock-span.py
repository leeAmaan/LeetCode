class StockSpanner:

    def __init__(self):
        self.stack = [[inf, 0]]
        
        

    def next(self, price: int) -> int:
        curDay = self.stack[-1][1]+1
        print(curDay)
        while price >= self.stack[-1][0]:
            self.stack.pop(-1)
            
        span = curDay-self.stack[-1][1]
        
        self.stack.append([price, curDay])
        
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)