class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        dictT = defaultdict(int)
        for c in t:
            dictT[c] += 1

        required = len(dictT)
        left, right = 0, 0
        formed = 0

        windowCounts = defaultdict(int)
        ans = [-1, 0, 0]

        while right < len(s):
            c = s[right]
            windowCounts[c] += 1

            if c in dictT and windowCounts[c] == dictT[c]:
                formed += 1

            while left <= right and formed == required:
                c = s[l]

                if ans[0] == -1 or right - left + 1 < ans[0]:
                    ans[0] = right - left + 1
                    ans[1] = left
                    ans[2] = right

                windowCounts[c] -= 1
                if c in dictT and windowCounts[c] < dictT[c]:
                    formed -= 1

                left += 1

            right += 1

        return "" if ans[0] == -1 else s[ans[1]:ans[2] + 1]
