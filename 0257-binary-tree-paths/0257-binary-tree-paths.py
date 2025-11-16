# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def search(root,ans,path):
            if not root:
                return 
            if not path:
                path+=str(root.val)+"->"
            else:
                path+=str(root.val)+"->"
            if not root.left and not root.right:
                ans.append(path)
            search(root.left,ans,path) 
            search(root.right,ans,path)   
            path=path[0:len(path)-1]
            path=path[0:len(path)-1]





        ans=[]
        path=""
        search(root,ans,path)
        return [item[0:len(item)-2] for item in ans]
        