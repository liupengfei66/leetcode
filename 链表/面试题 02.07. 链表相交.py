# https://leetcode-cn.com/problems/intersection-of-two-linked-lists-lcci/
# 这题最重要的还是观察题目本身，因此有交点就意味着交点以后的结点都是一样的
# 因此，如果从尾到头来看，我们只需要从位置相同的地方逐一比较即可

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        fastA, fastB = headA, headB
        slowA, slowB = headA, headB
        lenA, lenB = 0, 0
        while fastA:
            lenA += 1
            fastA = fastA.next
        while fastB:
            lenB += 1
            fastB = fastB.next

        if lenB > lenA:
            for _ in range(lenB - lenA):
                slowB = slowB.next
        else:
            for _ in range(lenA - lenB):
                slowA = slowA.next

        while slowA:
            if slowA == slowB:
                return slowA
            slowA = slowA.next
            slowB = slowB.next

        return None


# 解法2：这个思路非常巧妙
# A长度为 a, B长度为b， 假设存在交叉点，此时 A到交叉点距离为 c， 而B到交叉点距离为d
# 后续交叉后长度是一样的，那么就是 a-c = b-d -> a+d = b+c
# 这里意味着只要分别让A和B额外多走一遍B和A，那么必然会走到交叉，注意这里边缘情况是，大家都走到null依然没交叉，那么正好返回null即可
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
        根据快慢法则，走的快的一定会追上走得慢的。
        在这道题里，有的链表短，他走完了就去走另一条链表，我们可以理解为走的快的指针。

        那么，只要其中一个链表走完了，就去走另一条链表的路。如果有交点，他们最终一定会在同一个
        位置相遇
        """
        cur_a, cur_b = headA, headB  # 用两个指针代替a和b

        while cur_a != cur_b:
            cur_a = cur_a.next if cur_a else headB  # 如果a走完了，那么就切换到b走
            cur_b = cur_b.next if cur_b else headA  # 同理，b走完了就切换到a

        return cur_a
