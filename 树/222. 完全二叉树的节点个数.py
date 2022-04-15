# https://leetcode-cn.com/problems/count-complete-tree-nodes/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# 解法1：利用完全二叉树性质，完全二叉树=满二叉树的组合
# 递归的找完全二叉树，即左右子树深度相等，如果不相等，就继续往下层找
# 最终如果是单结点，一定是完全二叉树
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        left, right = root.left, root.right
        left_depth, right_depth = 0, 0
        while left:
            left = left.left
            left_depth += 1
        while right:
            right = right.right
            right_depth += 1
        if left_depth == right_depth:
            # 完全二叉树的结点数量计算方法，2^depth - 1
            return (2 << left_depth) - 1
        return self.countNodes(root.left) + self.countNodes(root.right) + 1

# 解法2：跟104一样，采取后序遍历的方法
# 先计算左右子树结点数量，然后加上中间结点
class Solution:
    def getNodeNum(self, root: TreeNode):
        if not root:
            return 0
        left = self.getNodeNum(root.left)
        right = self.getNodeNum(root.right)
        nodeNum = left + right + 1
        return nodeNum
    def countNodes(self, root: TreeNode) -> int:
        return self.getNodeNum(root)

# 解法3：跟104一样，直接利用层次遍历法，然后记录结点数量即可。

