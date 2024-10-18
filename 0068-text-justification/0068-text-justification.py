class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result=[]
        cur_line=[]
        words.append("x" * (maxWidth+1))
        cur_len = 0
        cur_words = 0
        for s in words:
            if cur_words==0:
                cur_line.append(s)
                cur_len += len(s)
                cur_words +=1
            elif (cur_len+len(s)+1) > maxWidth:
                req_spaces = maxWidth - cur_len
                if cur_words == 1 or s==words[-1]:
                    cur_line.append(" "*req_spaces)
                    result.append("".join(cur_line))
                else:
                    remaining = req_spaces%(cur_words//2)
                    req_spaces //= (cur_words//2)
                    for idx in range(1, cur_words, 2):
                        if remaining:
                            cur_line[idx]+= " "*(req_spaces + 1)
                            remaining -= 1
                        else:
                            cur_line[idx]+= " "*req_spaces
                    result.append("".join(cur_line))
                cur_line = [s]
                cur_len, cur_words = len(s), 1
            else:
                cur_line.append(" ")
                cur_line.append(s)
                cur_len += len(s)+1
                cur_words +=2
        return result     