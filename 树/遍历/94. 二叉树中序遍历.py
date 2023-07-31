# https://leetcode-cn.com/problems/binary-tree-inorder-traversal/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 递归
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def traversal(root):
            if not root:
                return root
            traversal(root.left)
            res.append(root.val)
            traversal(root.right)
        traversal(root)
        return res

# 迭代
# 思路与前序差不多，就是先遍历完左子树，然后访问结点值，再遍历右子树
# 不同之处在于，访问结点的顺序不同
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = []
        curr = root
        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                res.append(curr.val)
                curr = curr.right
        return res

# Morris遍历
# 核心是完善前驱关系，与前序的Morris方法基本一致
# 不同之处在于，curr.val的加入时机不同，前序是第一次建立链接时，而中序是左子树遍历完返回时
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        curr = root
        while curr:
            predecessor = curr.left
            if predecessor:
                while predecessor.right and predecessor.right != curr:
                    predecessor = predecessor.right
                if predecessor.right == curr:
                    res.append(curr.val)
                    predecessor.right = None
                    curr = curr.right
                else:
                    predecessor.right = curr
                    curr = curr.left
            else:
                res.append(curr.val)
                curr = curr.right
        return res