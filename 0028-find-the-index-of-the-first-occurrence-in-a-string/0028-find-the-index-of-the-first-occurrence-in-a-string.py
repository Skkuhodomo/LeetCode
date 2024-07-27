class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle)==0:
            return 0
        i=0
        while i<(len(haystack)-len(needle))+1:
            if haystack[i:i+len(needle)]!=needle:
                i+=1
            else:
                return i

        return -1    