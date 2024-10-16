class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        We can use a monotonic decreasing stack to store daily temperature  and the day index.

        1. Initialise stack as [0] which will store days in descending temperature which have yet to 
        see a greater temperature, and result as list of 0's length n.

        2. Then move to next day. Compare day temp to top of stack. If temp is greater than top of 
        stack, pop from top of stack. Then at the index of the day at top of stack, insert into results
        the diff between that index and current index.

        3. Loop until current day temp is less than or equal to top of stack then append to stack.
        
        """
    
        n = len(temperatures)
        stack = [0]
        result = [0 for _ in range(n)]

        for i in range(1, n):
            # Compare day_i temp to those at top of stack, pop until it is not greater than any values
            while stack and temperatures[stack[-1]] < temperatures[i]:
                # Day which we have found higher temp for 
                j = stack.pop()
                result[j] = i - j
            stack.append(i)
            
        return result