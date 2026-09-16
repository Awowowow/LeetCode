# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        dummy = ListNode(0, head)
        curr = head
        prev = dummy

        while curr and curr.next:
            front = curr.next
            forward = front.next
            prev.next = front
            front.next = curr
            curr.next = forward
            prev = curr
            curr = forward
        return dummy.next