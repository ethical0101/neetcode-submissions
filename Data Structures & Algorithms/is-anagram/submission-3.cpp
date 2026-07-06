class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> freq;

        if(s.length() != t.length()){
            return false;
        }

        for(char x : s){
            freq[x]++;
        }

        for(char y : t){
            freq[y]--;
            if(freq[y]<0){
                return false;
            }
        }
       
        return true;
    }
};
