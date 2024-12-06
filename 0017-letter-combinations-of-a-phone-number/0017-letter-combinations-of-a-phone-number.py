class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        phone = {'2': 'abc', '3': 'def', '4':'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        result = []
        def backtrack(i, s):
            for letter in phone[digits[i]]:
                s.append(letter)
                if len(s)==len(digits):
                    result.append("".join(s))
                else:
                    backtrack(i+1, s)
                s.pop()
        backtrack(0, [])
        return result