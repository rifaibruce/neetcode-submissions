class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        We are given an integer array nums
        We are given an integer k 
        We are to return the kth most frequent elements within the array

        Example: We are given nums = [1,2,2,3,3,3]
                 We are given k = 2
                 We are to return the 2 most frequent elemnts within the array
        Ok we can assume the answer is always unique and we can return the answer in any    order
        I am thinking I can set up a hash table with an entry being the number of frequencies of a number in nums and the index being the number in nums and then return an array of the numbers
        Algo goes like this:
        1. Initialize empty hash table
        2. Loop over array 
        3. For each element in array use it as an index in the hash table
        4. Count the elment and save the count as an entry in the hash table 
        5. Based on k return the k most frequent elements within the array
        """
        count_dict = {}
        sorted_dict = {}
        ans_arr = []
        for num in nums:
            count_dict[num] = 0
        for num in nums:
            count_dict[num] += 1
        for key in sorted(count_dict, key=count_dict.get):
            sorted_dict[key] = count_dict[key]
        for i in range(k):
            ans_arr.append(sorted_dict.popitem()[0])
        return ans_arr



