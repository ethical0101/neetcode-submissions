class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> mp;
        vector<vector<string>> ans;

        for(string i: strs){
            string copy = i;
            sort(i.begin(), i.end());
            mp[i].push_back(copy);
        }

        for(auto &it:mp){
            ans.push_back(it.second);
        }

        return ans;
    }
};
