class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        int n = nums.size();
        vector<vector<int>> bucket(n+1);
        vector<int> result = {};


        unordered_map<int, int> map;
        for(int i=0; i<nums.size(); i++) {
            map[nums[i]]++;
        }

        for(auto i: map) {
            bucket[i.second].push_back(i.first);
        }

        for(int i=bucket.size()-1; i>=0; i--) {
            if(bucket[i].size() > 0) {
                for(int j=0; j<bucket[i].size(); j++) {
                    result.push_back(bucket[i][j]);
                    if(result.size() == k) {
                        return result;
                    }
                }
            }
        }
    }
};
