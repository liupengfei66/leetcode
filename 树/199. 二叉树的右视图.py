# https://leetcode-cn.com/problems/binary-tree-right-side-view/
# 层次遍历，每层最右边，也就是最后一个元素，加入最终结果
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
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
            res.append(tmp[-1])
        return res