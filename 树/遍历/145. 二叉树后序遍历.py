# https://leetcode-cn.com/problems/binary-tree-postorder-traversal/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
# 1. 递归
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def traversal(root):
            if not root:
                return root
            traversal(root.left)
            traversal(root.right)
            res.append(root.val)
        traversal(root)
        return res

# 迭代
# 左子树全部压入栈，右子树也全部压入栈
# 如果右子树为空，开始输出结点值
# 同时记录下已经输出的值，避免重复输出
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        stack = []
        curr = root
        prev = None
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            # 右孩子为空或已经访问过，输出当前结点值
            # 如果输出，证明其左右子树都访问过了，需要置为空，否则下一个循环会继续访问其左子树
            if not curr.right or curr.right == prev:
                res.append(curr.val)
                prev = curr
                curr = None
            # 右孩子不为空，压栈，转向右子树
            else:
                stack.append(curr)
                curr = curr.right
        return res

# 迭代
# 这种方法可以实现结果，但本质上是前序的逆，并不是真正的后序遍历
# 因为前序是中左右，而后续是右左中，所以只要按照中右左，然后逆序即可
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack = [root]
        result = []
        while stack:
            node = stack.pop()
            # 中结点先处理
            result.append(node.val)
            # 左孩子先入栈
            if node.left:
                stack.append(node.left)
            # 右孩子后入栈
            if node.right:
                stack.append(node.right)
        # 将最终的数组翻转
        return result[::-1]

# 3. Morris
# 其他都与前中序的Morris一样，只是在输出时有些区别
# 后序遍历是左右中，因此在addPath中，加入左的时候，是每次加入当前及其右孩子，因此需要逆序
# 左孩子是作为单独结点加入进去的
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        def addPath(node):
            count = 0
            while node:
                res.append(node.val)
                node = node.right
                count += 1
            start, end = len(res)-count, len(res)-1
            while start < end:
                res[start], res[end] = res[end], res[start]
                start += 1
                end -= 1
        res = []
        curr = root
        while curr:
            predecessor = curr.left
            if predecessor:
                while predecessor.right and predecessor.right != curr:
                    predecessor = predecessor.right
                if predecessor.right == curr:
                    predecessor.right = None
                    addPath(curr.left)
                    curr = curr.right
                else:
                    predecessor.right = curr
                    curr = curr.left
            else:
                curr = curr.right
        # 根节点及其右孩子都不在结果中
        addPath(root)
        return res