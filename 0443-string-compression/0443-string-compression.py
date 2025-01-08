class Solution:
    def compress(self, chars: List[str]) -> int:
        left=0
        i=0
        while i<len(chars):
            length=1
            while ((i+length)<len(chars) and chars[i+length]==chars[i]):
                length+=1
            chars[left]=chars[i]
            i+=length
            left+=1
            if(length>1):
                # if len > 10 we need to add each digit
                for j in list(str(length)):
                    chars[left]=j
                    left+=1    
        return left