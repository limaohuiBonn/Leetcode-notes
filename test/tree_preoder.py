class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        node_ls = []
        def dfs(cur):
            if cur == None:
                return
            node_ls.append(cur.val)
            dfs(cur.left)
            dfs(cur.right)
        
        dfs(root)
        return node_ls