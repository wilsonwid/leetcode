class Solution {
public:
    bool backspaceCompare(string s, string t) {
        // need left and right pointers for each string
        // if # encountered, then need to move the left pointer back
        // and move the right pointer forward
        // else s[left] = s[right]
        int l1 = 0, r1=0, l2=0, r2=0;

        while (r1 < s.length()) {
            if (s[r1] == '#') {
                l1 = max(l1-1, 0);
                r1++; 
            } else {
                s[l1] = s[r1];
                l1++;
                r1++;
            }
        }

        while (r2 < t.length()) {
            if (t[r2] == '#') {
                l2 = max(l2-1, 0);
                r2++;
            } else{
                t[l2] = t[r2];
                l2++;
                r2++;
            }
        }
        
        return l1 == l2 && s.substr(0, l1) == t.substr(0, l2);
    }
};
