# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root):
        queue = collections.deque([[root]])
        res = []
        while queue:
            curr_layer = queue.popleft()
            next_layer = []
            curr_value = []
            for node in curr_layer:
                curr_value.append(node.val)
                if node.left:
                    next_layer.append(node.left)
                if node.right:
                    next_layer.append(node.right)
            if not next_layer:
                queue.append(next_layer)
            if not curr_value:
                res.append(curr_value)
        return res

s= Solution()

left = TreeNode(9)
right=TreeNode(20)
root=TreeNode(3, left, right)
s.levelOrder(root)