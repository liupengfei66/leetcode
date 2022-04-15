# https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
# 对比于236，本题因为是BST简单很多，只要根节点在左右孩子的区间内，那么就满足结果
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 解法1：迭代，因为原题并没有说明p和q哪个大，所以需要满足p<=root<=q和q>=root>=q都可以
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
            if root.val > p.val and root.val > q.val:
                root = root.left
            elif root.val < p.val and root.val < q.val:
                root = root.right
            else:
                return root
        return None

# 解法2：递归
# 递归的思路与迭代法也差不多，注意与235的区别是不用遍历整棵树，找到立即返回即可
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
            if root.val > p.val and root.val > q.val:
                return self.lowestCommonAncestor(root.left, p ,q)
            if root.val < p.val and root.val < q.val:
                return self.lowestCommonAncestor(root.right, p ,q)
            return root