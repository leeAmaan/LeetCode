class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        
        for i in ops: 
            if i not in "CD+":
                stack.append(int(i))
            elif i =="C":
                stack.pop()
            elif i == "D":
                stack.append(2*stack[-1])
            elif i == "+":
                stack.append(stack[-2] + stack[-1])
        
        return sum(stack)
                    