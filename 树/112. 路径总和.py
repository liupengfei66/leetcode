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
        if not root:
            return False

        def traversal(root, cnt):
            # 到达叶结点
            if not root.left and not root.right:
                if cnt == 0:
                    return True
                else:
                    return False

            if root.left:
                cnt -= root.left.val  # 递归，cnt代入下层处理
                if traversal(root.left, cnt):
                    return True
                cnt += root.left.val  # 回溯，cnt回归原样
            if root.right:
                cnt -= root.right.val
                if traversal(root.right, cnt):
                    return True
                cnt += root.right.val
            return False

        return traversal(root, targetSum - root.val)

# 迭代，前序遍历寻找路径和，栈里的元素是一个pair对，存储了当前的结点以及路径和
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        stack = [(root, root.val)]
        while stack:
            curr = stack.pop()
            node, val = curr
            if not node.left and not node.right and val==targetSum:
                return True
            if node.right:
                stack.append((node.right, val+node.right.val))
            if node.left:
                stack.append((node.left, val+node.left.val))

        return False