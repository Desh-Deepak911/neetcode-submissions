class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_map<int, int> map;
        bool duplicate = false;
        for(int i=0; i < nums.size(); i++) {
            map[nums[i]]++;
        }

        for(auto i: map) {
            if(i.second > 1)
                duplicate = true;
        }
        return duplicate;
    }
};
