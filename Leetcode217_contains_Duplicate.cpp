class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        
        unordered_map <int, int> frequencies; 
        
        for (int i = 0; i < nums.size(); i++){
            frequencies[nums[i]]++; 
            
        }
        
        for(auto & i: frequencies){
            if (i.second >= 2){
                return true; 
            }
            
        }
        
        return false; 
        
    }
};
