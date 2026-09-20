"""
I am given an array of numbers 
I need to output an array of numbers where each index in the output array is 
the product of all other numbers without the number in index i
example: input is [1,2,3] output is [6,3,2]
I am thinking that I can just calculate the product of all the terms in the array and then divide by the index i in the input array
So the algorithm looks like this:
Initialize total_product to one
Initialize output_arr to empty list
For each number in input_arr:
    total_product = total_prodcut * input_arr[i]
For each number in input_arr:
    output_arr[i] = total_product / input_arr[i]
return output_arr
I did not think of the edge case when 0 is a member of the array 
Now we have three main cases
1. No zeroes
2. One zero
3. More than one zero
For the no zeroes one we just use the old algorithm
For the one zero one we just use the modification of having a product of all the non zero terms be in the zero index
For the more than one zero one we just return an array of the same length as the input array filled with zeroes

Now I will try to solve it without the division operator
For the two zero cases it is easy as I just have to return the total product and an array of zeroes, in the case of no zeroes I am thinking of calcualting the product each time on an array that has that value spliced out
So new algo is:
Init total_product = 1
Init total_product_excluding_zero = 1
Init output_arr to empty arr
Init zeroes counter to number of zeroes in arr

If zero_counter > 1:
    return array of zeroes
If zero_counter == 1:
    return array of zeroes except in the index of zeroes have the total_product_excluding_zero
else:
    for each num:
        create new array without the num 
        get the total product of the array 
        save it in the output array at num 

I know have read the hints and know that a better way without using the division operator is to use two arrays one that has the left product and one that has the right product and then multiply them together

So the algorithm is:
Init output_arr
Init left_product_arr
Init right_product_arr
Init left_total_product
Init right total_product

for each number in nums:
    calculate the product of all the numbers left to that number
    put the product in the left_product_arr in the same index as the num

for each number in nums:
    calculate the product of all the numbers right to that number
    put the product in the right_product_arr in the same index as the num

for each number in nums:
    multiply the same index of left_product_arr and right_product_arr and save them in output_arr

return output_arr
"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output_arr = []
        left_product_arr = [1] * n
        right_product_arr = [1] * n

        for i in range(1, n):
            left_product_arr[i] = left_product_arr[i-1] * nums[i -1]
        
        for i in range(n - 2, -1, -1):
            right_product_arr[i] = right_product_arr[i+1] * nums[i+ 1]
        
        return [left_product_arr[i] * right_product_arr[i] for i in range(n)]