# https://leetcode-cn.com/problems/invert-binary-tree/
# 左右翻转二叉树

# 这题只要能遍历树的方法，都可以。遍历到每个结点，交换其左右孩子即可。
# 中序的时候，要注意写法，比较容易错，以递归为例，因为中序结点是先左再中
# 以root为例，当遍历到root时，root的左子树中，其实已经翻转过一次了，此时到root，进行左右孩子交换，左子树变为了右子树
# 那么如果此时再按照左中右遍历，那又到了原先的左子树了，画个简单的图就明白了

# 解法1：迭代，先交换左右子树，再交换左孩子的左右孩子，再交换右孩子的左右孩子
import collections
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

# 解法2：迭代，前序遍历，遍历到每个结点，就交换其左右孩子
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        stack = [root]
        while stack:
            curr = stack.pop()
            curr.left, curr.right = curr.right, curr.left
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)
        return root

# 解法3：层次遍历
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        queue = collections.deque([root])
        while queue:
            curr = queue.popleft()
            curr.left, curr.right = curr.right, curr.left
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        return root