class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1 = defaultdict(list)
        for word in strs:
            count = [0]*26
            for i in word:
                count[ord(i) - ord("a")] += 1
            dict1[tuple(count)].append(word)
        return dict1.values()
        