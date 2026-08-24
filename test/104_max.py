class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0
        def dfs(cur):
            nonlocal depth 
            if cur == None:
                return
            depth += 1
            dfs(cur.left)
            dfs(cur.right)

        dfs(root)
        return depth

