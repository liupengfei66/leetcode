# https://leetcode-cn.com/problems/reverse-linked-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 解法1：迭代
# 定义多个指针，分别负责前一个结点，当前结点，和下一个结点
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr, next = None, head, None
        while curr:
            next = curr.next
            curr.next = prev
            prev, curr = curr, next
        return prev

# 解法2：递归
# 首先，递归的终止条件为，只有1个结点或没有结点，那么就返回该结点或空，都可以表达为head
# 其次，对一个需要反向的链表，我们可以先反向其剩余部分，即head.next
# 如果剩余部分都已经反向了，那么当前我们只需要将head.next.next=head，就可以实现整个列表的反向
# 最后，由于此时head.next依然是正向的，需要设置为空，可以画图理解下
# 关于这个解法，代码录上写的不是很好，参考官方答案
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # 假设1->2->3，当执行到2，假设3已经被反转
        # 那么对于2应该执行2.next.next=2, 2.next=None
        # 而对于3，因为是最后一个结点了，直接返回就行
        # 以2，3两步之间的联动和关系，应该就可以写出整个代码
        if not head or not head.next:
            return head
        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return new_head