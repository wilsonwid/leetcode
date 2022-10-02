class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        word_dict = {}
        for letter in p:
            word_dict[letter] = word_dict.get(letter, 0) + 1
        lst = []
        initial_string = s[0:len(p)]
        string_dict = {}
        for letter in initial_string:
            string_dict[letter] = string_dict.get(letter, 0) + 1
        for i in range(len(s) - len(p) + 1):
            if word_dict == string_dict:
                lst.append(i)
            string_dict[s[i]] = string_dict[s[i]] - 1
            if (string_dict[s[i]] == 0):
                del string_dict[s[i]]
            try:
                string_dict[s[i+len(p)]] = string_dict.get(s[i+len(p)], 0) + 1
            except:
                continue
            
        return lst
