# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, t: str) -> Optional[TreeNode]:
        st = []
        n = len(t)
        i = 0
        
        while i<n:
            d = 0

            while i<n and t[i] == "-":
                d += 1
                i += 1
            
            val = 0

            while i<n and t[i].isdigit():
                val*= 10
                val += int(t[i])
                i += 1
            
            while st and st[-1][0] >= d:
                st.pop()
            
            node = TreeNode(val)

            if st:
                parentNode = st[-1][1]
                if not parentNode.left:
                    parentNode.left = node
                else:
                    parentNode.right = node
            st.append((d, node))
        
        return st[0][1]