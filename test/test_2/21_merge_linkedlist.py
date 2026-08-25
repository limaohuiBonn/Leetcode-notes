class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        merged_list = ListNode()
        cur = merged_list
        cur_i = list1
        cur_j = list2
        while cur_i != None and cur_j != None:
            if cur_i.val < cur_j.val:
                cur.next = cur_i
                cur_i = cur_i.next
                cur = cur.next
            else:
                cur.next = cur_j
                cur_j = cur_j.next
                cur = cur.next

        cur.next = cur_i if cur_i != None else cur_j
        return merged_list.next
            
