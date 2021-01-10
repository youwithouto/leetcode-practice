class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        map, result = {}, []
        for i in nums1:
            if i in map:
                map[i] += 1
            else:
                map[i] = 1
        for j in nums2:
            if j in map and map[j] != 0:
                result.append(j)
                map[j] -= 1
        return result
