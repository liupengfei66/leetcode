# https://leetcode-cn.com/problems/delete-node-in-a-bst/
# 递归，删除结点涉及到树结构的调整，调整方法如下
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # 遍历到空结点，返回，即没找到需要删除的结点
        if not root:
            return root
        # 找到需要删除的结点
        if root.val == key:
            # 1. 左右孩子为空，直接删除，返回空
            if not root.left and not root.right:
                return None
            # 2. 左孩子为空，将右孩子提升上来
            elif not root.left:
                return root.right
            # 3. 右孩子为空，将左孩子提升上来
            elif not root.right:
                return root.left
            # 4. 左右孩子都不为空，将左子树放到右子树的最左侧，然后右孩子代替原结点
            else:
                curr = root.right
                while curr.left:
                    curr = curr.left
                curr.left = root.left
                return root.right
        # 递归处理子树
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        return root


