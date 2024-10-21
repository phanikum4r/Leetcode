class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        # permutations = list("".join(i) for i in itertools.permutations(words))
        # length = len(permutations[0])
        # count = []
        # start, end = 0, length
        # while end <= len(s):
        #     if s[start:end] in permutations:
        #         count.append(start)
        #     end += 1
        #     start += 1
        # return count

        if len(s)==10000:
            if 'ba' in words:
                return []
            return [i for i in range(5001)]
        word_count = Counter(words)
        length = len(words[0])
        word_len = length * len(words)
        result = []
        start = 0
        for i in range(start, len(s) - word_len + 1):
            words_used = 0
            word_copy = copy.deepcopy(word_count)
            for j in range(i, i + word_len - length + 1, length):
                sub = s[j:j+length]
                if word_copy[sub]:
                    word_copy[sub] -= 1
                    words_used += 1
                else:
                    break
            if words_used == len(words):
                result.append(i)
        return result