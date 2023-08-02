# https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/
# 给定一个二叉树，找出其最小深度。

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 方法一：递归
# 与104的区别主要是要考虑左右子树中有一个为空的情况
class Solution:
    def getDepth(self, root: TreeNode):
        if not root:
            return 0
        left_depth = self.getDepth(root.left)
        right_depth = self.getDepth(root.right)
        if left_depth == 0 or right_depth == 0:
            depth = 1 + max(left_depth, right_depth)
        else:
            depth = 1 + min(left_depth, right_depth)
        return depth
    def minDepth(self, root: TreeNode) -> int:
        return self.getDepth(root)

# 方法二：非迭代
# 也是层次遍历，遍历到左右子树都为空的时候，就可以退出了
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        res = []
        queue = collections.deque([root])
        while queue:
            tmp = []
            for i in range(len(queue)):
                curr = queue.popleft()
                tmp.append(curr)
                if not curr.left and not curr.right:
                    return len(res) + 1
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            res.append(tmp)
        return len(res)
