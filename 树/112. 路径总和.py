# https://leetcode-cn.com/problems/path-sum/
# 这题跟257基本一致，只是稍微有所不同
# 递归，有返回值
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def traversal(root, total):
            if not root:
                return False
            total += root.val
            if not root.left and not root.right:
                if total == targetSum:
                    return True
            left = traversal(root.left, total)
            right = traversal(root.right, total)
            if left or right:
                return True
            else:
                return False
        return traversal(root, 0)

# 迭代，前序遍历寻找路径和，栈里的元素是一个pair对，存储了当前的结点以及路径和
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        stack = [(root, root.val)]
        while stack:
            curr = stack.pop()
            node, total = curr
            if not node.left and not node.right and total == targetSum:
                return True
            if node.right:
                stack.append((node.right, total+node.right.val))
            if node.left:
                stack.append((node.left, total+node.left.val))
        return False