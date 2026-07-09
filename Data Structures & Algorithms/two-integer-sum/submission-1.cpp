class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> res;
        for(int i = 0; i < nums.size(); i++){
            int require = target - nums[i];
            if(res.find(require) != res.end()){
                return {res[require], i};
            }
            res[nums[i]] = i;
        }
        return {};
    }
};
