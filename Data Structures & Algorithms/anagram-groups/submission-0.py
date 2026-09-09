class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_dict = defaultdict(list)
        for str in strs:
            sorted_str = "".join(sorted(str))
            strs_dict[sorted_str].append(str)
        return list(strs_dict.values())