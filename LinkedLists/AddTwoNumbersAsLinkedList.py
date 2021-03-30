class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = temp = ListNode(0)
        carry = 0
        while l1 or l2 or carry!=0:
            sum=0
            if l1:
                sum += l1.val
                l1=l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            sum += carry
            carry = sum//10
            node = ListNode(sum%10)
            temp.next = node
            temp = temp.next
        return dummy.next