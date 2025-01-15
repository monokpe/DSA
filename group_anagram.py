from collections import defaultdict


class Solution:
    def group_anagrams(self, strs: list[str]) -> list[list[str]]:
        anagram_map = {}
        for str in strs:
            count = [0] * 26
            for char in str:
                count[ord(char) - ord("a")] += 1

            key = tuple(count)
            anagram_map.setdefault(key, []).append(str)

        return list(anagram_map.values())


class Solution2:
    def group_anagrams(self, strs: list[str]) -> list[list[str]]:
        result = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            result[tuple(count)].append(s)
        return list(result.values())


ana = Solution2()
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print("Here are your anagrams:", ana.group_anagrams(strs))
