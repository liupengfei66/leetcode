# https://leetcode-cn.com/problems/convert-bst-to-greater-tree/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 递归，这题是BST，所以遍历顺序是右中左，然后累加即可，右中左是反中序遍历
# 如果把BST的中序遍历理解为一个递增数组，那么本题就是从数组末尾到开头，逐个累加即可
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.pre_val = 0
        def traversal(root):
            if not root:
                return
            traversal(root.right)
            root.val += self.pre_val
            self.pre_val = root.val
            traversal(root.left)
        traversal(root)
        return root

