class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        I have to check if a duplicate exists in an integer array
        I am thinking I can create a data structure that has as its indexes each number in the array
        So that means that I go through the array and for each number I create an index in the other data structure and hold in it the count of the number
        So this means that for each number in the array I have to first check if it exists in the other data struct, if it does then I found a duplicate and I can return true, otherwise I create an index and update the count to one 
        Ok so the Algorithm is:
        0. Create the other data structure and have it be empty
        1. Loop through the array
        2. For each number in the array, check if it is in the other data structure
        3. If it is in the other data structure return true 
        4. If not create an index with the number and have its count incremented 
        5. If at end of array and haven't returned true return false
        """
        num_table = {}
        for num in nums:
            if num in num_table:
                return True
            num_table[num] = 1
        return False

        