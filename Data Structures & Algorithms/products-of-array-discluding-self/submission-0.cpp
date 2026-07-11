class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int len = nums.size();
        vector<int> Left(len, 0);
        vector<int> Right(len, 0);
        vector<int> res(len, 0);
        Left[0] = 1;
        Right[len - 1] = 1;

        for(int i = 1; i < len ; i++){
            Left[i] = Left[i-1] * nums[i-1];
        }

        for(int j = len - 1; j > 0 ; j--){
            Right[j - 1] = Right[j] * nums[j];
        }

        for(int k = 0; k < len ; k++){
            res[k] = Left[k] * Right[k];
        }

        return res;

    }
};