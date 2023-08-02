# https://leetcode-cn.com/problems/search-in-a-binary-search-tree/
# 给定二叉搜索树（BST，左<中<右）的根节点 root 和一个整数值 val。
# 你需要在 BST 中找到节点值等于 val 的节点。 返回以该节点为根的子树。 如果节点不存在，则返回 null 。

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 解法1：递归，注意，如果elif和else不加return，那就是搜索整棵树了
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root or root.val == val:
            return root
        elif root.val > val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)

# 解法2：迭代
# 由于二叉搜索树的特性，本题用迭代特别的简单...
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        while root:
            if root.val == val:
                return root
            elif root.val > val:
                root = root.left
            else:
                root = root.right
        return None