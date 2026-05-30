class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        prefList = [1 for _ in range(n)]
        suffList = [1 for _ in range(n)]
        
        result = []

        for i in range(n):
            if i == 0:
                continue
            print("PrefList " + str(i))
            prefList[i] = nums[i-1] * prefList[i-1]
            print("PrefList "+ str(prefList[i]))
        print(prefList)
        for i in range(n - 1, -1, -1):
            if i == n-1:
                continue
            print("Suff index" + str(i))
            suffList[i] = nums[i+1] * suffList[i+1]
            print("SuffList " + str(suffList[i]))
        print(suffList)
        for i in range(n):
            prod = prefList[i] * suffList[i]
            result.append(prod)
        return result
