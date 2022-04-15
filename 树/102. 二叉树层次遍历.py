# https://leetcode-cn.com/problems/binary-tree-level-order-traversal/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 借助队列实现，对每一层，按照顺序进入队列
# 每有一个出队列，将其左右孩子放入队列，实现层次顺序遍历
# collections.deque是一个高效的双端队列，在popleft时，时间复杂度为O(1)
# 而list.pop(0)，复杂度是O(n)，因为要移动0之后所有的元素
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root:
            return res
        queue = collections.deque([root])
        while queue:
            tmp = []
            n_queue = len(queue)
            for i in range(n_queue):
                curr = queue.popleft()
                tmp.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            res.append(tmp)
        return res

# 解法2：递归
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root:
            return res
        def traversal(root, deepth):
            if not root:
                return []
            if len(res) == deepth:
                res.append([])
            res[deepth].append(root.val)
            if root.left:
                traversal(root.left, deepth+1)
            if root.right:
                traversal(root.right, deepth+1)

        traversal(root, 0)
        return res