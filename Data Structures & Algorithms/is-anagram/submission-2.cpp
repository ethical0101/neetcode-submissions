class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> mapone;
        unordered_map<char, int> maptwo;

        if(s.length() < t.length() || s.length() > t.length()){
            return false;
        }

        for(int i = 0; i < s.length() ; i++){
            mapone[s[i]]++;
        }
        for(int i = 0; i < t.length() ; i++){
            maptwo[t[i]]++;
        }

        if(mapone != maptwo){
            return false;
        }
       
        return true;
    }
};
