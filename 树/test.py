# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root, targetSum: int) :
        if not root:
            return []

        def traversal(root, path, res, cnt):
            # 在当前结点处理当前逻辑，返回后，需要回溯这两个处理
            path.append(root.val)
            cnt -= root.val
            # 到达叶子结点，符合条件，添加结果，不符合条件，直接返回
            if not root.left and not root.right:
                if cnt == 0:
                    # 注意这里要是复制，否则引用了同一个path，否则会被后面的操作修改
                    res.append(path[:])
                return
            if root.left:
                traversal(root.left, path, res, cnt)
                path.pop()
                cnt += root.left.val
            if root.right:
                traversal(root.right, path, res, cnt)
                path.pop()
                cnt += root.right.val
        cnt = 0
        path, res = [], []
        traversal(root, path, res, targetSum)
        return res
s = Solution()
node7=TreeNode(7)
node2=TreeNode(2)
node8=TreeNode(8)
node11=TreeNode(11, node7, node2)
node4=TreeNode(4, node11)
root = TreeNode(5, node4, node8)

s.pathSum(root, 22)
