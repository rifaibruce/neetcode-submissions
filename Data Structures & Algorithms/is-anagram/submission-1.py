class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if s == t:
            return True
        first_str_hash = {}
        for letter in s:
            if letter in first_str_hash:
                first_str_hash[letter] = first_str_hash[letter] + 1
            else:
                first_str_hash[letter] = 1
        for letter in t:
            if letter in first_str_hash:
                first_str_hash[letter] = first_str_hash[letter] - 1
            else:
                return False
        for entry in first_str_hash:
            if first_str_hash[entry] != 0:
                return False
        
        return True
