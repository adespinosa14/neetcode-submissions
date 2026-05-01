class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for str in strs:
            res += str
            res += "#29"

        return res
        

    def decode(self, s: str) -> List[str]:
        
        decoded = s.split("#29")
        decoded.pop()
        
        return decoded
