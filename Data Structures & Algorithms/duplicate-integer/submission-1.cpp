class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        map<int, int> duplicates;
        for(int i : nums){
            if(duplicates[i] >= 1){
                return true;
            }
            duplicates[i]++;
        }
    return false;
    }
};