class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for val in strs:
            res += str(len(val)) + "#" + val
        return res # 2#bo3#qwe2##e --> [bo , qwe, #e]

    def decode(self, s: str) -> List[str]:
        list1 = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            list1.append(s[j+1 : j+1+length])
            i = j + 1 + length
        return list1
        

            
