# https://leetcode-cn.com/problems/trim-a-binary-search-tree/
# 给你二叉搜索树的根节点 root ，同时给定最小边界low 和最大边界 high。通过修剪二叉搜索树，使得所有节点的值在[low, high]中。
# 修剪树 不应该 改变保留在树中的元素的相对结构 (即，如果没有被移除，原有的父代子代关系都应当保留)。 可以证明，存在 唯一的答案 。
                                                                                                  
# 递归，这题与450基本一致，但是要注意，修改后的树，依然要进行剪枝，不能直接返回了
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        if not root:
            return root
        if root.val < low or root.val > high:
            if not root.left and not root.right:
                return None
            elif not root.left:
                return self.trimBST(root.right , low, high)
            elif not root.right:
                return self.trimBST(root.left, low, high)
            else:
                tmp = root.right
                while tmp.left:
                    tmp = tmp.left
                tmp.left = root.left
                return self.trimBST(root.right, low, high)
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        return root

# 解法2：递归
# 本题也可以不那么复杂，如果当前结点小于low，那么就修剪其右子树
# 如果当前结点大于high，就修剪其左子树
# 最后把修剪完的左右子树，赋值给当前结点即可
class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        if not root:
            return root
        # 如果根节点都小于low，那么根节点及其左子树都小于low
        # 直接返回右子树修剪的结果即可，因为根节点及其左子树肯定都要删掉的
        if root.val < low:
            return self.trimBST(root.right, low, high)
        # 同理
        if root.val > high:
            return self.trimBST(root.left, low, high)
        # 如果根节点满足条件，那就递归的处理其左右子树
        # 不管怎么删，只要根节点不被删，左右子树肯定还在左右子树内，这是BST的性质
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        return root