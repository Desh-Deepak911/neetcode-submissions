class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        n = len(nums)
        freqList = [[] for _ in range(n + 1)]
        hm = {}
        ans = []

        for n in nums:
            hm[n] = 1 + hm.get(n, 0)
        
        for i, n in hm.items():
            freqList[n].append(i)
        for i in range(len(freqList) - 1, 0, -1):
            for n in freqList[i]:
                ans.append(n)
                if len(ans) == k:
                    return ans;
             




        