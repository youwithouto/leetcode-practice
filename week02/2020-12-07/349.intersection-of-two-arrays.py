class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        map, result = {}, []
        for i in nums1:
            map[i] = True
        for j in nums2:
            if j in map:
                del map[j]
                result.append(j)
        return result
