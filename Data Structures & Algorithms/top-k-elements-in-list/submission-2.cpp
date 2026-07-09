#include <algorithm>

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        // unordered_map<int, int> mp;

        map<int, vector<int>, greater<int>> mp;
        vector<int> res;
        sort(nums.begin(), nums.end());
        int i = 0;

        while(i<nums.size()){
            int j = i;

            while(j < nums.size() && nums[i] == nums[j]){
                j++;
            }

            int count = j - i;
            mp[count].push_back(nums[i]);
            i=j;
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
