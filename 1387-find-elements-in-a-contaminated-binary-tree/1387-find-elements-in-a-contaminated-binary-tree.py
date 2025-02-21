# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.arr = set()
        def change(root,v):
            if not root:
                return
            self.arr.add(v)
            change(root.left,(2*v)+1)
            change(root.right,(2*v)+2)
        change(root,0)

        

    def find(self, target: int) -> bool:
        return target in self.arr

