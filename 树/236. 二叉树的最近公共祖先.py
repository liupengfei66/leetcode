# https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/
# 首先，终止条件：我们找到了p或q，或到达叶结点，那么就返回该结点
# 其次，单层递归：我们找到左右子树中是否包含p和q，如果分别在左右子树，那么当前就是最近的公共祖先，否则一定是都在左子树或都在右子树，题目说了p和q为树中结点
# 最后，如果都在左子树，那么我们就返回左子树，继续递归的查找
# 同理，如果都在右子树，就返回右子树，继续递归的查找
# 这题的方法在于，首先我们从上往下寻找，找到p或q时，我们在返回时，将p或q给带上来
# 也就是在返回的过程中，不断的将p或q往上提升，最终在最近公共祖先处，左右子树的结果都是非空的了
# 如果提前找到了，那么一个子树一定是空，此时只返回非空子树的结果即可。

# 这题可以这么理解：每个结点，都接收左右子树的状态，然后判断是否符合祖先结点的条件
# 因为是递归调用，所以找到后，也是带着已有的结果，逐层返回
# 这题是假设p,q一定都是存在的，例如下面这个例子，如果是查找5,4。
# 那么直接从3开始，查到左子树，返回5；查到右子树，返回空，就直接返回了5，并没有向下继续查找了
#     3
#  5      1
# 6  2  0  8
#   7 4
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        elif left:
            return left
        else:
            return right
