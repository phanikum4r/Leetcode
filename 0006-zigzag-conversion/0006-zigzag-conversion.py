class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        n = len(s)
        curRow = 0
        result = []
        #no of elements between next element of 0th row
        section_length = 2 * (numRows - 1)
        for curRow in range(numRows):
            index = curRow
            while index<n:
                result.append(s[index])

                if curRow!=0 and curRow<numRows-1:
                    cur_section_length = section_length - 2*curRow
                    if index+cur_section_length<n:
                        result.append(s[index+cur_section_length])
                
                index += section_length
        return "".join(result)
