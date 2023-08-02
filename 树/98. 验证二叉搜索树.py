# https://leetcode-cn.com/problems/validate-binary-search-tree/
# 给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。
# 有效 二叉搜索树定义如下：
# 节点的左子树只包含 小于 当前节点的数。
# 节点的右子树只包含 大于 当前节点的数。
# 所有左子树和右子树自身必须也是二叉搜索树。

# 这题其实超级无敌简单，只要你想明白，BST就是按中序遍历，结果是否递增，那么此题就非常简单了

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 解法1：递归，你也可以按迭代做一遍，因为是纯练习中序遍历，所以这里就不再迭代方法了
class Solution:

    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return False
        res = []

        def traversal(root):
            if not root:
                return
            traversal(root.left)
            res.append(root.val)
            traversal(root.right)

        traversal(root)
        for i in range(len(res) - 1):
            if res[i] >= res[i + 1]:
                return False
        return True

# 解法2：迭代，中序遍历
class Solution:
    def isValidBST(self, root):
        stack = []
        cur = root
        pre = None  # 记录前一个节点
        while cur is not None or len(stack) > 0:
            if cur is not None:
                stack.append(cur)
                cur = cur.left  # 左
            else:
                cur = stack.pop()  # 中
                if pre is not None and cur.val <= pre.val:
                    return False
                pre = cur  # 保存前一个访问的结点
                cur = cur.right  # 右
        return True