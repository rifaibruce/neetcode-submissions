class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for i in range(len(nums)):
            nums_dict[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in nums_dict:
                if nums_dict[complement] == i:
                    continue
                return [i, nums_dict[complement]]
        return []




