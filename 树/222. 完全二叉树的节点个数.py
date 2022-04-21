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
# 时间复杂度O(logn*logn)，空间复杂度O(logn)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        def cTree(root):
            if not root:
                return 0
            left = root.left
            right = root.right
            l_h, r_h = 0, 0
            while left:
                l_h += 1
                left = left.left
            while right:
                r_h += 1
                right = right.right
            # 左右高度相等，表明是一颗完全二叉树
            if l_h == r_h:
                return (2 << l_h) - 1
            # 高度不相等，分别递归其左右子树，然后加上根节点
            else:
                return cTree(root.left) + cTree(root.right) + 1
        return cTree(root)


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

