class Solution {
public:

    string encode(vector<string>& strs) {
        string encodedStr = "";
        for(int i=0; i<strs.size(); i++) {
            encodedStr += to_string(strs[i].length())+'#'+strs[i];
        }
        return encodedStr;
    }

    vector<string> decode(string s) {
        vector<string> result;
        
        int i = 0;
        while (i < s.size()) {
            int j = i;
            while (s[j] != '#') {
                j++;
            }
            int length = stoi(s.substr(i, j - i));
            string str = s.substr(j + 1, length);
            result.push_back(str);
            i = j + 1 + length;
        }
        
        return result;
    }
};
