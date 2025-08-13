class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        intersection = []
        hashmap = {}
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1  # 交換，保證 nums1 比較短

        for n in nums1:
            hashmap[n] = hashmap.get(n, 0) + 1 # 統計次數

        for n in nums2:
            count = hashmap.get(n, 0)
            if count > 0:
                hashmap[n] = count - 1 # 統計次數
                intersection.append(n)

        return intersection
