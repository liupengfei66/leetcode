# https://leetcode-cn.com/problems/insert-into-a-binary-search-tree/
# 给定二叉搜索树（BST）的根节点 root 和要插入树中的值 value ，将值插入二叉搜索树。 
# 返回插入后二叉搜索树的根节点。 输入数据 保证 ，新值和原始二叉搜索树中的任意节点值都不同。


# 解法1：递归，核心思想是：对于BST，结点插入位置就是按遍历顺序的空结点位置
# BST的插入不涉及结构调整
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        if root.val > val:
            root.left = self.insertIntoBST(root.left, val)
        if root.val < val:
            root.right = self.insertIntoBST(root.right, val)
        return root

# 解法2：迭代
# 设定一个指向其父节点的指针，方便找到位置后进行插入
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        curr, parent = root, root
        while curr:
            parent = curr
            if curr.val > val:
                curr = curr.left
            else:
                curr = curr.right

        if parent.val > val:
            parent.left = TreeNode(val)
        else:
            parent.right = TreeNode(val)
        return root