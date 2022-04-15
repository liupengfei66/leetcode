# https://leetcode-cn.com/problems/swap-nodes-in-pairs/
# 如果设置了虚拟头结点，那么整个链表的交换就遵循同一个逻辑
# 只要想通了这里，还是比较简单的。需要画图，否则容易给绕晕的
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        res = ListNode(next=head)
        pre = res

        # 必须有pre的下一个和下下个才能交换，否则说明已经交换结束了
        while pre.next and pre.next.next:
            cur = pre.next
            post = pre.next.next

            # pre，cur，post对应最左，中间的，最右边的节点
            cur.next = post.next
            post.next = cur
            pre.next = post

            pre = pre.next.next
        return res.next