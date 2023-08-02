# https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/
# 给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
# 对于有根树 T 的两个节点 p、q，最近公共祖先表示为一个节点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）


# 这题可以这么理解：每个结点，都接收左右子树的状态，然后判断是否符合祖先结点的条件
# 因为是递归调用，所以找到后，也是带着已有的结果，逐层返回
# 这题是假设p,q一定都是存在的，例如下面这个例子，如果是查找5,4。
# 那么直接从3开始，查到左子树，返回5；查到右子树，返回空，就直接返回了5，并没有向下继续查找了
# 如果p或q有一个不存在，那么就会只返回存在的那个节点本身，例如p不存在，结果就是返回q
#     3
#  5      1
# 6  2  0  8
#   7 4
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

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

if __name__ == '__main__':
    node7 = TreeNode(7)
    node4 = TreeNode(4)
    node2 = TreeNode(2, node7, node4)
    node6 = TreeNode(6)
    node5 = TreeNode(5, node6, node2)
    node0 = TreeNode(0)
    node8 = TreeNode(8)
    node1 = TreeNode(1, node0, node8)
    node3 = TreeNode(3, node5, node1)

    node9 = TreeNode(9)

    solution = Solution()
    res = solution.lowestCommonAncestor(node3, node9, node7)
    if res:
        print("ancestor:", res.val)
    else:
        print("no ancestor")