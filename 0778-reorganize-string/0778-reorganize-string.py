class Solution:
    def reorganizeString(self, s: str) -> str:
        # chars=Counter(s)
        # sorted_chars = sorted(chars.items(), key = lambda x: -x[1])
        # if sorted_chars[0][1]>(len(s)+1)//2:
        #     return ""
        # res=[""]*len(s)
        # idx=0
        # for char, count in sorted_chars:
        #     for _ in range(count):
        #         res[idx]=char
        #         idx+=2
        #         if idx>=len(s):
        #             idx=1
        # return "".join(res)

        max_heap = [(-count,char) for char, count in Counter(s).items()]
        heapq.heapify(max_heap)
        res=[]

        while max_heap:
            count, char = heapq.heappop(max_heap)
            if len(res)==0 or res[-1]!=char:
                res.append(char)
                if count+1<0:
                    heapq.heappush(max_heap,(count+1,char))
            elif res[-1]==char:
                if (len(max_heap)==0):
                    return ""
                nextcount, nextchar = heapq.heappop(max_heap)
                res.append(nextchar)
                res.append(char)
                if count+1<0:
                    heapq.heappush(max_heap,(count+1,char))
                if nextcount+1<0:
                    heapq.heappush(max_heap,(nextcount+1,nextchar))
        return "".join(res)