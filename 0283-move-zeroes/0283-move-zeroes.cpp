class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int i=0,j=1;
        while (i<nums.size() && j<nums.size()){
            if (nums[i]==0 && nums[j]!=0){
                swap(nums[i],nums[j]);
                i+=1;
            }
            else if(nums[i]!=0){
                i+=1;
            }
            j+=1;
        }
    }
};