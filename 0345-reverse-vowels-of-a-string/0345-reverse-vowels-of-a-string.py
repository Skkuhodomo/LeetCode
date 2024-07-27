class Solution:
    def reverseVowels(self, s: str) -> str:
        # 큐를 시용해 시간 복잡도가 O(n)인 알고리즘 
        vs = set("aeiouAEIOU") # 모음의 집합 
        v = [c for c in s if c in vs] # 모음 중, s에 있는 것 리스트로 
        res = ""
        for c in s:
            if c in vs:
                res += v.pop()
            else:
                res += c
        return res