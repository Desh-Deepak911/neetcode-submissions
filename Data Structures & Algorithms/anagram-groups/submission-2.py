class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashMap = defaultdict(list) # mapping charCount to string arrays

        for string in strs:
            count = [0] * 26

            for ch in string:
                count[ord(ch) - ord("a")] += 1
            
            hashMap[tuple(count)].append(string)
        
        return list(hashMap.values())
