class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int p=1, n=nums.size();
        vector<int> answer(n);
        for(int i=0;i<n;i++){
            answer[i]=p;
            p*=nums[i];
        }
        p=1;
        for(int i=n-1;i>=0;i--){
            answer[i]*=p;
            p*=nums[i];
        }
        return answer;
    }
};