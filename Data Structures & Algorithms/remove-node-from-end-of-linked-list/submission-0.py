# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #one loop to get the length of linked list
        cur_length = 0
        curr = head
        while curr:
            cur_length += 1
            curr = curr.next
        new_n = cur_length - n
        if new_n == 0:
            return head.next
        curr = head
        prev = None
        incrementer = 0
        #Now to remove that node
        while curr:
            if incrementer == new_n:
                prev.next = curr.next
                break
            else:
                incrementer += 1
                prev = curr
                curr = curr.next
        return head
