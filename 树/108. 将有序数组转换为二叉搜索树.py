# https://leetcode-cn.com/problems/convert-sorted-array-to-binary-search-tree/
# 给你一个整数数组 nums ，其中元素已经按 升序 排列，请你将其转换为一棵 高度平衡 二叉搜索树。
# 高度平衡 二叉树是一棵满足「每个节点的左右两个子树的高度差的绝对值不超过 1 」的二叉树。

# 解法1：递归
# 因为原数组是有序的，且构建的BST可以多种，所以这题就是按数组的中间作为根节点，左右数组作为左右子树构建就好了
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        n_nums = len(nums)
        if n_nums == 0:
            return None
        if n_nums == 1:
            return TreeNode(nums[0])
        mid = n_nums // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[0:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root