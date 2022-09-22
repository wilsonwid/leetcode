class Solution {
public:
    string reverseWords(string s) {
        string newString = "";
        int i = 0; 
        string currWord = "";
        while (i < s.length()) {
            if (s.at(i) == ' ') {
                for (int j = 0; j < currWord.length(); j++) {
                    newString += currWord.at(currWord.length() - j - 1);
                }
                currWord = "";
                newString += ' ';
            } else {
                currWord += s.at(i);
            }
            if (i == s.length() - 1 && s.at(i) != ' ') {
                for (int j = 0; j < currWord.length(); j++) {
                    newString += currWord.at(currWord.length() - j - 1);
                }
            }
            i++;
        }
        return newString;
    }
};
