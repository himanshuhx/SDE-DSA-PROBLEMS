# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Note - Node given is not tail node
# if tail case than use if else to keep check
# e.g 1->2->3->4 node given to delete 4
# if not node.next: (that means tail node)
#       node.val = None (make it null)
class Solution:
    def deleteNode(self, node):
        node.val=node.next.val
        node.next=node.next.next