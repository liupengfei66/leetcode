# https://leetcode-cn.com/problems/binary-tree-paths/
# 输出二叉树从根节点到叶子节点的所有路径

# 解法1：递归，采用前序遍历方法，注意递归的时候的终止条件变了，因为本题需要找到叶子结点，就开始处理逻辑了
# 注意path的回溯逻辑，每当一个递归处理完成，递归自身会回溯回来，path也应该完成相应的回溯
# 可以根据leetcode上的例子，手动模拟一下path的回溯过程
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 利用字符串传参实现回溯
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def traversal(root, path):
            if not root:
                return

            # 叶结点，不需要添加->
            if not root.left and not root.right:
                path += str(root.val)
                res.append(path)
            else:
                path += str(root.val) + "->"
            traversal(root.left, path)
            traversal(root.right, path)

        res = []
        traversal(root, "")
        return res

# 解法2：迭代，也是采用前序遍历，也是终止条件不同
# 迭代法是在第一次访问时，就固定了每个结点的路径，这样下面的结点就不受其他影响
# 是比较符合我们直觉的一种方法
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        stack, path_stack, res = [root], [str(root.val)], []
        while stack:
            curr = stack.pop()
            path = path_stack.pop()
            if not curr.left and not curr.right:
                res.append(path)
            if curr.right:
                stack.append(curr.right)
                path_stack.append(path + '->' + str(curr.right.val))
            if curr.left:
                stack.append(curr.left)
                path_stack.append(path + '->' + str(curr.left.val))
        return res


