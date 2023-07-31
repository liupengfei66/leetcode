# https://leetcode-cn.com/problems/binary-tree-level-order-traversal-ii/
# 层次遍历，但是自底向上输出

import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# 层次遍历，最后翻转一下结果即可
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        queue = collections.deque([root])
        while queue:
            tmp = []
            for i in range(len(queue)):
                curr = queue.popleft()
                tmp.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            res.append(tmp)
        return res[::-1]