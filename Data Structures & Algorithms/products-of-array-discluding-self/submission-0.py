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
"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_product = 1
        total_product_excluding_zero = 1
        output_arr = []
        zeroes_counter = 0

        for num in nums:
            if num == 0:
                zeroes_counter += 1
        if zeroes_counter > 1:
            for num in nums:
                output_arr.append(0)
            return output_arr
        elif zeroes_counter == 1:
            for num in nums: 
                if num == 0:
                    continue
                total_product_excluding_zero *= num
            for num in nums:
                if num == 0:
                    output_arr.append(total_product_excluding_zero)
                else:
                    output_arr.append(0)
        else:
            for num in nums:
                total_product *= num
            for num in nums:
                output_arr.append(int(total_product / num))

        
        return output_arr 