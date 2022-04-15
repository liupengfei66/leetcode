# https://leetcode-cn.com/problems/symmetric-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 大体来说，判断方法都是，先判断左右子树，如果不符合条件，就直接返回
# 如果符合条件，就继续判断左右子树，先比较左子树的左节点和右子树的右节点，即外面两个结点相同
# 再比较左子树的右结点和右子树的左节点
# 解法一：递归
class Solution:
    def compare(self, left: TreeNode, right: TreeNode):
        # 有一个结点为空，或两个结点数值不等，不用进入子树
        if not left and not right:
            return True
        elif left and not right:
            return False
        elif not left and right:
            return False
        elif left.val != right.val:
            return False
        else:  # 两个结点都不为空，且数值相等，继续判断子树
            outside = self.compare(left.left, right.right)
            inside = self.compare(left.right, right.left)
            return outside and inside

    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return root
        return self.compare(root.left, root.right)

# 迭代，思路与递归差不多，也是先比较外侧，再比较内侧
# 借助层次遍历的思想，但是加入队列的顺序是方便比较的顺序，而不是遍历顺序
# 队列换成栈也行
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        queue = collections.deque([root.left, root.right])
        while queue:
            left = queue.popleft()
            right = queue.popleft()
            if not left and not right:
                continue
            if not left or not right or left.val != right.val:
                return False

            queue.append(left.left)
            queue.append(right.right)
            queue.append(left.right)
            queue.append(right.left)

        return True
