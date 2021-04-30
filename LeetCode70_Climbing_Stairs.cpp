class Solution {
public:
    int climbStairs(int n) {
        vector<unsigned int> dp; 
        if (n == 2){
            return 2; 
        }
        if (n ==1){
            return 1; 
        }
    
        dp.push_back(1);  //base cases
        dp.push_back(2); 
        
        for(int i =2; i<n+1; i++){
            dp.push_back(dp[i-1] + dp[i-2]);
            
        }
        return (dp[n-1]); 
        
        
    }
};
