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

        # if len(s)==10000:
        #     if 'ba' in words:
        #         return []
        #     return [i for i in range(5001)]
        # word_count = Counter(words)
        # length = len(words[0])
        # word_len = length * len(words)
        # result = []
        # start = 0
        # for i in range(start, len(s) - word_len + 1):
        #     words_used = 0
        #     word_copy = copy.deepcopy(word_count)
        #     for j in range(i, i + word_len - length + 1, length):
        #         sub = s[j:j+length]
        #         if word_copy[sub]:
        #             word_copy[sub] -= 1
        #             words_used += 1
        #         else:
        #             break
        #     if words_used == len(words):
        #         result.append(i)
        # return result

        if not s or not words:
            return []
        
        word_length = len(words[0])
        total_concat_length = word_length * len(words)
        word_count = Counter(words)
        
        result_indices = []
        
        # Check for all possible starting points in the first `word_length` characters
        for i in range(word_length):
            left = i
            seen_words = Counter()
            count = 0  # To track the number of valid words we've seen in the current window
            
            # Slide through the string with steps of `word_length`
            for right in range(i, len(s) - word_length + 1, word_length):
                current_word = s[right:right + word_length]
                
                if current_word in word_count:
                    seen_words[current_word] += 1
                    count += 1
                    
                    # If we have seen more of `current_word` than required, shrink the window from the left
                    while seen_words[current_word] > word_count[current_word]:
                        left_word = s[left:left + word_length]
                        seen_words[left_word] -= 1
                        count -= 1
                        left += word_length
                    
                    # If the window size matches the number of words, we have a valid concatenation
                    if count == len(words):
                        result_indices.append(left)
                        
                        # Move the window forward by removing the leftmost word
                        left_word = s[left:left + word_length]
                        seen_words[left_word] -= 1
                        count -= 1
                        left += word_length
                else:
                    # If current_word is not a valid word, reset the window
                    seen_words.clear()
                    count = 0
                    left = right + word_length
        
        return result_indices