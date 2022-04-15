# https://leetcode-cn.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
# 思路其实比较简单，就是根据后序遍历的最后一个元素确认根节点
# 然后根据中序遍历和根节点，确认左右子树。
# 然后对左右子树分别递归上述步骤即可。
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder or not postorder:
            return None

        # 根据后序的最后一个元素，找到左右子树，然后分别遍历
        # 1. 根据后序，找到中间结点
        root_val = postorder[-1]
        root = TreeNode(root_val)
        # 终止条件，后序遍历中只有1个元素，返回该元素
        if len(postorder) == 1:
            return root
        # 2. 根据中序，找到左右子树
        idx_mid = inorder.index(root_val)
        left_inorder = inorder[0: idx_mid]
        right_inorder = inorder[idx_mid+1:]
        # 3. 根据中序中左右子树长度，找到后序的左右子树
        left_postorder = postorder[0: idx_mid]
        right_posterorder = postorder[idx_mid: -1]
        # 4. 递归调用
        root.left = self.buildTree(left_inorder, left_postorder)
        root.right = self.buildTree(right_inorder, right_posterorder)
        return root
