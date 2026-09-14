class Solution:
    """
    I am given a list of strings
    I am to encode the list of strings as one str 
    I am then to decode the str into the previous list of strings

    The main problem is how the decode procedure will know how to reconstruct the str into the
    list strs


    """
    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return "\0"
        return " \n".join(strs)

    def decode(self, s: str) -> List[str]:
        if s == "\0":
            return []
        return s.split(" \n")
