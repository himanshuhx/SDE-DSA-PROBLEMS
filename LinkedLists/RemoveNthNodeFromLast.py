# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# TWO PASS SOLUTION
# APPROACH - First loop to get length of linkedList
# after getting length using second loop get to desired node i.e length-n will be our desired node from start
# remove the link curr.next = curr.next.next or we can maintain a prev pointer too
# IMPORTANT (EDGE CASE) - if length-n == head than return head.next
# EX - list - [1] , n ==1 |  o/p - []

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head:
            return
        length, temp = 0, head
        while temp:
            temp = temp.next
            length += 1
        if n == length:
            head = head.next
            return head
        temp = prev = head
        for i in range(length - n):
            prev = temp
            temp = temp.next
        prev.next = temp.next
        return head

# Using Fast and slow Pointer
# move fast to nth node
# move slow and fast together until fast.next != null
# break the link slow.next = slow.next.next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head:
            return
        dummy = ListNode(0)
        dummy.next = head
        fast = slow = dummy
        for i in range(n):
            fast = fast.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummy.next
