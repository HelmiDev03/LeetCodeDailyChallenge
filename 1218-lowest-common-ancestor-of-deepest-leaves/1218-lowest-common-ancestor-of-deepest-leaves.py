class Solution:
    def lcaDeepestLeaves(self, r: Optional[TreeNode]) -> Optional[TreeNode]:
        def f(n):
            if not n: return 0,None
            ld, ln, rd, rn = *f(n.left), *f(n.right)
            return ((ld+1,n),(ld+1,ln),(rd+1,rn))[(ld>rd)-(ld<rd)]

        return f(r)[1]