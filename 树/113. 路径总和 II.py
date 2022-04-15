# https://leetcode-cn.com/problems/path-sum-ii/
# 递归
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []

        def traversal(root, path, res, cnt):
            # cnt写在这里不行，写在这里，相当于是在下一层减了val
            # 但是int的实参传递的值，因此，在上层还是2，返回后+val
            # 就变成了cnt+val，而不是cnt-val+val
            # path因为是传递的引用，所以写在这里也可以，因为下一层的修改对本层也有效
            # 或者，你可以利用值传递的特性，返回时不用加回来，因为值传递，其实已经加回来了
            path.append(root.val)
            # cnt -= root.val
            # 到达叶子结点，符合条件，添加结果，不符合条件，直接返回
            if not root.left and not root.right:
                if cnt == 0:
                    # 注意这里要是复制，否则引用了同一个path，否则会被后面的操作修改
                    res.append(path[:])
                return
            if root.left:
                cnt -= root.left.val
                traversal(root.left, path, res, cnt)
                path.pop()
                cnt += root.left.val
            if root.right:
                cnt -= root.right.val
                traversal(root.right, path, res, cnt)
                path.pop()
                cnt += root.right.val
        path, res = [], []
        traversal(root, path, res, targetSum-root.val)
        return res

# 注意与上面的不同，就是cnt是值传递，在调用函数和返回函数时，其实相当于自动实现了回溯效果
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []

        def traversal(root, path, res, cnt):
            # cnt写在这里不行，写在这里，相当于是在下一层减了val
            # 但是int的实参传递的值，因此，在上层还是2，返回后+val
            # 就变成了cnt+val，而不是cnt-val+val
            # path因为是传递的引用，所以写在这里也可以，因为下一层的修改对本层也有效
            # 或者，你可以利用值传递的特性，返回时不用加回来，因为值传递，其实已经加回来了
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
            if root.right:
                traversal(root.right, path, res, cnt)
                path.pop()
        path, res = [], []
        traversal(root, path, res, targetSum)
        return res

# 这题还可以用迭代的方法做，比较简单，参照112和257即可，就不再练习了
