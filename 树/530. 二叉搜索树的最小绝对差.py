# https://leetcode-cn.com/problems/minimum-absolute-difference-in-bst/
# 给你一个二叉搜索树的根节点 root ，返回 树中任意两不同节点值之间的最小差值 。
# 差值是一个正数，其数值等于两值之差的绝对值。

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 这题跟98其实一样，只要想到用中序遍历，剩下就是求递增数组的差值就行了
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        if not root:
            return 0
        nodes = []
        def traversal(root):
            if not root:
                return
            traversal(root.left)
            nodes.append(root.val)
            traversal(root.right)
        traversal(root)
        res = float("inf")
        for i in range(len(nodes)-1):
            res = min(res, abs(nodes[i]-nodes[i+1]))
        return res

