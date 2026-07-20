class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        prev_right = 0
        

        while left <= right:
            mid = ((right - left) // 2) + left
            if nums[mid] == target:
                return mid

            if nums[mid] > target:
                prev_right = right
                right = mid - 1
            else:
                left = mid + 1

        return left

        