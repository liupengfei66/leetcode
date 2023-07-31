# https://leetcode-cn.com/problems/binary-tree-preorder-traversal/
# Definition for a binary tree node.
from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# 1. 递归
# 时间复杂度O(n) - 每个结点被遍历一次
# 空间复杂度O(n) - 最坏情况呈现链状，栈的开销为O(n)
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def traversal(root):
            if root:
                res.append(root.val)
                traversal(root.left)
                traversal(root.right)
        traversal(root)
        return res

# 2. 迭代 - 栈
# 采用这种迭代方法，可以保持前中序的代码一致
# 这种解法更符合直觉，也就是先遍历左边的子树，再遍历右边的子树
# 先记录根节点，即根节点入栈，然后遍历左子树，左子树遍历完，弹出根节点，遍历右子树
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        while stack or root:
            if root:
                res.append(root.val)
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                root = root.right
        return res

# 迭代 - 栈
# 因为前序遍历是中左右，所以进栈顺序是右左,出栈时对应左右
# 采用这种方法，可以保持前后序的方法一致
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # 根结点为空则返回空列表
        if not root:
            return []
        stack = [root]
        result = []
        while stack:
            node = stack.pop()
            # 中结点先处理
            result.append(node.val)
            # 右孩子先入栈
            if node.right:
                stack.append(node.right)
            # 左孩子后入栈
            if node.left:
                stack.append(node.left)
        return result

# 3. Morris - predecessor
# 时间复杂度O(n)，空间复杂度O(1)
# Morris的核心思想是找到每个结点的前驱结点，从而代替栈，节省空间
# 1. 如果当前结点的左子树为空，将当前结点输出，并移动到右子树
# 2. 如果当前结点的左子树不为空，找到左孩子中，最右边的结点，如果该结点其右子树为空，建立关系并输出当前结点；
# 3. 如果其右子树等于当前结点，证明已经访问过，断掉关系，并移动到右子树
# Morris最核心的是利用predecessor处理了左右子树的情况
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        curr = root
        while curr:
            # 考虑其左孩子，因为其左子树的最右节点，一定在其直接左孩子里产生
            predecessor = curr.left
            # 如果左孩子存在
            if predecessor:
                # 找到最右结点，为防止无限循环，需要不等于当前结点
                while predecessor.right and predecessor.right != curr:
                    predecessor = predecessor.right
                # 如果已经建立过链接，那么证明左子树已经遍历完，当前是从其左孩子的最右结点过来的，所以转向右子树
                if predecessor.right == curr:
                    predecessor.right = None
                    curr = curr.right
                # 如果没有，证明第一次建立链接，并且是第一次访问当前结点，建立后，转向左孩子
                # 在写代码时，可以先写else部分，逻辑比较清楚
                else:
                    predecessor.right = curr
                    res.append(curr.val)
                    curr = curr.left
            else:
                res.append(curr.val)
                curr = curr.right
        return res