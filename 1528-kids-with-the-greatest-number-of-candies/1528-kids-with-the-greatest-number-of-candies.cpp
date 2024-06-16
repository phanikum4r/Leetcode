class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        int m = *max_element(candies.begin(),candies.end()), n=candies.size();
        vector<bool> result(n);
        for(int i=0; i<n; i++){
            if(candies[i]+extraCandies >= m){
                result[i]=true;
            }
        }
        return result;
    }
};