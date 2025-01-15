from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        for i in range(len(strs[0])):
            for s in strs[1:]:
                if i >= len(s) or s[i] != strs[0][i]:
                    return s[:i]
        return strs[0]


strs = []


solution = Solution()
result = solution.longestCommonPrefix(strs)
print(result)