class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}

        for index, num in enumerate(nums):
            remainder = target - num
            if remainder in nums_map:
                return [nums_map[remainder], index]
            else:
                nums_map[num] = index

