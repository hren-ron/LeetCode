'''

Given a string which contains only lowercase letters, remove duplicate letters so that every letter appear once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

Example:
Given "bcabc"
Return "abc"

Given "cbacdcbc"
Return "acdb"

Credits:
Special thanks to @dietpepsi for adding this problem and creating all test cases.
'''

class Solution {
public:
    string removeDuplicateLetters(string s) {
        int count[26] ={0};
        for (auto x : s)count[x-'a']++;
        string res;
        unordered_set<char> occur;
        for (auto t : s){
            if (!occur.count(t)){
                while (res.size() && count[res.back()-'a']>1 && res.back() > t){
                    count[res.back()-'a']--;
                    occur.erase(res.back());
                    res.pop_back();
                }
                res.push_back(t);
                occur.insert(t);
            }
            else count[t-'a']--;
        }
        return res;
    }
};
