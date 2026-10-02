# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        values = []
        current = head
        node_count = 1
        while current != None:
            if left <= node_count <= right:
                values.append(current.val)
            current = current.next
            node_count += 1
        node_count = 1
        current = head
        k = 0
        values.reverse()
        while current != None:
            if left <= node_count <= right:
                current.val = values[k]
                k += 1
            current = current.next
            node_count += 1
        return head