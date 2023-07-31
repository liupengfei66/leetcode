# https://leetcode-cn.com/problems/merge-two-binary-trees/
# 想象一下，当你将其中一棵覆盖到另一棵之上时，两棵树上的一些节点将会重叠（而另一些不会）。
# 你需要将这两棵树合并成一棵新二叉树。合并的规则是：如果两个节点重叠，那么将这两个节点的值相加作为合并后节点的新值；
# 否则，不为 null 的节点将直接作为新二叉树的节点。

# 这题与101类似，都是同时处理两棵树，可以递归的处理，比较容易想到
# 也可以采用队列，同时对两颗树进行处理
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 解法1：递归， 不改变原树
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if not root1:
            return root2
        if not root2:
            return root1
        root = TreeNode(root1.val + root2.val)
        root.left = self.mergeTrees(root1.left, root2.left)
        root.right = self.mergeTrees(root1.right, root2.right)
        return root

# 解法2：迭代法
import collections
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if not root1:
            return root2
        if not root2:
            return root1
        # 同时比较，所以同时压队列，很容易想到
        queue = collections.deque([root1, root2])

        while queue:
            node1 = queue.popleft()
            node2 = queue.popleft()
            node1.val += node2.val
            # 如果都存在左，那么就都压入队列
            if node1.left and node2.left:
                queue.append(node1.left)
                queue.append(node2.left)
            # 同理，如果都存在右，那么就都压入队列
            if node1.right and node2.right:
                queue.append(node1.right)
                queue.append(node2.right)
            # 如果root1的左不存在，而root2的左存在，那么就直接对root1.left补充root2.left
            if not node1.left and node2.left:
                node1.left = node2.left
            if not node1.right and node2.right:
                node1.right = node2.right

        return root1