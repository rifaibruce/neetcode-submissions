"""
I am given an array of integers nums
I am given a target, which is an integer
I want to find which two entries in the nums array add up to the target
I cannot return the same index, it has to be two different indexes
I am to return an array with the two indexes 

I am thinking first the brute force method is to have two loops 
The first loop takes in one index and the second loop adds in the entries in all following indexes

If we find the target then return the two indexes, else we move on to one more index 
This will need O(n^2) time complexity 


"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]