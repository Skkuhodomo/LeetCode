class Solution:
    def reverseVowels(self, s: str) -> str:
        vs = set("aeiouAEIOU")
        v = [c for c in s if c in vs]
        res = ""
        for c in s:
            if c in vs:
                res += v.pop()
            else:
                res += c
        return res