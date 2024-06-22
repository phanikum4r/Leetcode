class Solution {
public:
    int compress(vector<char>& chars) {
        int i=0, left=0, n=chars.size();
        while(i<n){
            int length=0;
            while((i+length)<n && (chars[i+length]==chars[i])){
                length+=1;
            }
            chars[left++]=chars[i];
            i+=length;
            if (length>1){
                for(char c : to_string(length)){
                    chars[left++]=c;
                }
            }
        }
        return left;
    }
};