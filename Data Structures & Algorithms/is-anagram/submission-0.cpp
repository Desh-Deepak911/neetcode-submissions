class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> netString;
        bool isAnagram = true;
        if(s.length() != t.length()) {
            return false;
        }

        for(int i=0; i<s.length(); i++) {
            netString[s[i]]++;
        }
        for(int i=0; i < t.length(); i++) {
            netString[t[i]]--;
        }
        for(auto i: netString) {
            if(i.second != 0){
                isAnagram = false;
            }
        }
        return isAnagram;
    }
};
