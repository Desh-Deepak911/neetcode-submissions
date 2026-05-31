class Solution:

    def encode(self, strs: List[str]) -> str:

        delimiter = "?!#"
        res = ""

        for s in strs:
            l = len(s)
            res += str(l) + delimiter + s
        
        return res


    def decode(self, s: str) -> List[str]:

        decodedList = []
        i = 0
        while i < len(s):
            delim_pos = s.find("?!#", i)
            charLength = int(s[i:delim_pos])
            start = delim_pos + 3
            word = s[start : start + charLength]
            decodedList.append(word)
            i = start + charLength
        
        return decodedList
