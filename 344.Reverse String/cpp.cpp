class Solution {
public:
    string reverseString(string s) {
        string ret = "";
        for (int i=s.size()-1; i>=0;i--){
            ret += s[i];   
        }
        return ret;
    }
};