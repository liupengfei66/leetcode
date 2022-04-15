# https://leetcode-cn.com/problems/minimum-absolute-difference-in-bst/
# Definition for a binary tree node.
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
        res = float(inf)
        for i in range(len(nodes)-1):
            res = min(res, abs(nodes[i]-nodes[i+1]))
        return res

