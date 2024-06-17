class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
       if(flowerbed.size()==1 ){
            if(flowerbed[0]==0 ){
                n-=1;
       }
       }
       else if(flowerbed[0]==0 && flowerbed[1]==0){
            flowerbed[0]=1;
            n-=1;
        }
        if(n==0){
            return true;
        }
       for(int i=1;i<flowerbed.size();i++){
        if(i==flowerbed.size()-1){
            if(flowerbed[i-1]==0 && flowerbed[i]==0){
                flowerbed[i]=1;
                n-=1;
            }
        }
        else if(flowerbed[i-1]==0 && flowerbed[i+1]==0 && flowerbed[i]==0){
            flowerbed[i]=1;
            n-=1;
        }
        if (n==0){
            return true;
        }
        
       } 
       return (n<=0)?true:false;

    }
};