"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []

        q, ans = deque([root]), []
    
        while q:
            level = []
            print(len(q))
            for i in range(len(q)):
                node = q.popleft()
                for child in node.children:
                    q.append(child)
                    #print(child)
                level += [node.val]
                #print(level)
            ans += [level]
            
        return ans
        
        
        
        
        
        
        #left.val = 
        #right.val = 
        #res = []
        #levelOrder():
            #res.append(s)
            