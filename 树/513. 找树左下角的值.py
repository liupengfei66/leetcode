# https://leetcode-cn.com/problems/find-bottom-left-tree-value/
# 给定一个二叉树的 根节点 root，请找出该二叉树的 最底层 最左边 节点的值。

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 层序遍历，
# 可以每次从右开始遍历到左，依次记录值，那么保留的就是最后一层最左边的
# 也可以从左到右遍历，但是每次只记录第一个值
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue = collections.deque([root])
        res = root.val
        while queue:
            n = len(queue)
            for _ in range(n):
                node = queue.popleft()
                res = node.val
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
        return res

# 解法2，递归
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        self.max_depth = 1
        self.res = root.val
        def traversal(root, depth):
            if not root:
                return
            # 叶结点
            if not root.left and not root.right:
                # 前序遍历，只有最左边的节点可能被执行
                if depth > self.max_depth:
                    self.res = root.val
                    self.max_depth = depth
            # depth作为参数，实际蕴含了回溯的思想
            # 使得高度可以随着递归而增加，随着返回而减少
            traversal(root.left, depth+1)
            traversal(root.right, depth+1)

        traversal(root, 1)
        return self.res