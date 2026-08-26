class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        merged_list = ListNode()
        cur = merged_list
        l1_pos = list1
        l2_pos = list2
        while l1_pos and l2_pos:
            if l1_pos.val < l2_pos.val:
                cur.next = l1_pos
                l1_pos = l1_pos.next
            else:
                cur.next = l2_pos
                l2_pos = l2_pos.next

            cur = cur.next

        cur.next = l1_pos if l1_pos else l2_pos

        return merged_list.next
