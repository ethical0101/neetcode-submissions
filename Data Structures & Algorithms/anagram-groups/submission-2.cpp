class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> mp;
        vector<vector<string>> ans;

        for(string &i: strs){  //& for not to copy the whole strings again 
            string copy = i;
            sort(copy.begin(), copy.end());
            mp[copy].push_back(i);
        }

        for(auto &it:mp){
            ans.push_back(it.second);
        }

        return ans;
    }
};
