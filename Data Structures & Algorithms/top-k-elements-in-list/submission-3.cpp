#include <algorithm>

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        // unordered_map<int, int> mp;

        unordered_map<int, int> freq;
        vector<int> res;

        map<int, vector<int> , greater<int>> mp;
        
        for(int x : nums){
            freq[x]++;
        }
        
        for(auto &it: freq){
            mp[it.second].push_back(it.first);
        }

        for(auto &it : mp){
            for(int x: it.second){
                res.push_back(x);

                if(res.size() == k){
                    return res;
                }
            }
        }

        return res;

    }
};
