class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_list = [[] for i in range(len(nums) + 1)]
        count_dict = {}

        for num in nums:
            count_dict[num] = 1 + count_dict.get(num, 0)
        for num, num_count in count_dict.items():
            freq_list[num_count].append(num)
        
        res = []
        for i in range(len(freq_list) - 1, 0, -1):
            for num in freq_list[i]:
                res.append(num)
                if len(res) == k:
                    return res
  



