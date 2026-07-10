class Solution {
public:

    string encode(vector<string>& strs) {
        string encoded_string = "";

        for(string s:strs){
            int len = s.length();
            encoded_string = encoded_string + to_string(len) + "#" + s;
        }

        return encoded_string;
    }

    vector<string> decode(string s) {
        vector<string> res;

        int i = 0;

        while(i<s.length()){
            int j = i;

            while(s[j] != '#'){
                j++;
            }

            int len = stoi(s.substr(i, j - i));

            string str = s.substr(j + 1 , len);

            i = j + 1 + len;

            res.push_back(str);
        }

        return res;
    }
};
