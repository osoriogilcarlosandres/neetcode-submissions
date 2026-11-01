class Solution:

    def encode(self, strs: List[str]) -> str:
        ren = ""
        for s in strs:
            ren += str(len(s)) + "@"+ s
        return ren
    def decode(self, s: str) -> List[str]:
        res = []
        p = 0
        while p < len(s):
            i = p
            while s[p]!= "@":
                p += 1
            length = int(s[i:p])
            res.append(s[p+1: p+1+length])
            p = p + 1 + length
        return res