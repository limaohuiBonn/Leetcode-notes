class Solution(object):
    def mergeTwoLists(self, list1, list2):
        merged_list = []
        i = 0
        j = 0
        while i < len(list1) and j < len(list2):
            if list1[i] < list2[j]:
                merged_list.append(list1[i])
                i += 1
            else:
                merged_list.append(list2[j])
                j += 1

        merged_list.extend(list1[i:])
        merged_list.extend(list2[j:])

        return merged_list
