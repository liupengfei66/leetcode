# https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 解法一：非递归，采用层次遍历法，顺便求出最大深度
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = [root]
        res = 0
        while queue:
            res += 1
            n = len(queue)
            for i in range(n):
                curr = queue.pop(0)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
        return res

# 解法二：递归 递归重点考虑终止条件，每个单层递归内的逻辑
# 可以假设最底层有一个结点，其左子树为空，右子树有1个结点
# 在这种情况下，比较容易想明白递归的逻辑
# 后序遍历，在中间结点处，求中间结点高度，因为root结点高度=树的深度，所以这种做法可以
class Solution:
    def getDepth(self, root: TreeNode):
        if not root:
            return 0
        left_depth = self.getDepth(root.left)
        right_depth = self.getDepth(root.right)
        depth = max(left_depth, right_depth) + 1  # +1是加上当前结点的高度
        return depth

    def maxDepth(self, root: TreeNode) -> int:
        return self.getDepth(root)

# 解法3：递归，前序遍历，求深度
class Solution:
    def __init__(self):
        self.res = 0

    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        def getDepth(root, depth):
            self.res = max(self.res, depth)
            if not root.left and not root.right:
                return
            if root.left:
                # 深入下一层，深度+1
                depth += 1
                getDepth(root.left, depth)
                # 回溯到上一层，深度-1
                depth -= 1
            if root.right:
                depth += 1
                getDepth(root.right, depth)
                depth -= 1
            return

        getDepth(root, 1)
        return self.res
