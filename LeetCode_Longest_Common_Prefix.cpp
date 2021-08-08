class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string prefix = strs[0];
        
        for(int i =0; i< strs.size(); i++){
            while(strs[i].find(prefix) != 0){
                if (prefix.length() == 0){
                    
                    return ""; 
                }
                prefix = prefix.substr(0, prefix.length()-1);
            }
        }
        return prefix; 
        
    
    }    
};
