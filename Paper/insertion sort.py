class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        nums = nums1+nums2
        nums.sort()
        if len(nums) % 2 != 0:
            return float(nums[int(len(nums)/2)])
        else:
            return (nums[int(len(nums)/2)] + nums[int(len(nums)/2)-1])/2
print(Solution().findMedianSortedArrays([1, 3], [2]))