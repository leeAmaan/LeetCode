"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        q, res = [root] if root else [], []
        while q:
            res.append([node.val for node in q])
            #print(ret)
            q = [child for node in q for child in node.children if child]
            #print(q)
        return res
        
        
        
        
        
        
        
        #left.val = 
        #right.val = 
        #res = []
        #levelOrder():
            #res.append(s)
            