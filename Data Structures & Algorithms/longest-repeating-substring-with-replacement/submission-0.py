class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        freqDict = {}
        l = 0
        longestSubstr = 0
        maxFreq = 0

        for r in range(len(s)):
            freqDict[s[r]] = freqDict.get(s[r], 0) + 1
            maxFreq = max(maxFreq, freqDict[s[r]])
            while (r - l + 1) - maxFreq > k:
                freqDict[s[l]] -= 1
                l += 1
            longestSubstr = max(longestSubstr, r - l + 1)
        return longestSubstr
            
        