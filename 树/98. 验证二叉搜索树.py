# https://leetcode-cn.com/problems/validate-binary-search-tree/
# 这题其实超级无敌简单，只要你想明白，BST就是按中序遍历，结果是否递增，那么此题就非常简单了
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 解法1：递归，你也可以按迭代做一遍，因为是纯练习中序遍历，所以这里就不再迭代方法了
class Solution:

    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return False
        res = []

        def traversal(root):
            if not root:
                return
            traversal(root.left)
            res.append(root.val)
            traversal(root.right)

        traversal(root)
        for i in range(len(res) - 1):
            if res[i] >= res[i + 1]:
                return False
        return True
