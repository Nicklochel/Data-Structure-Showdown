# Timed Challenge Problem
# Question: "Given a string, return the first non-repeating character. 
# If all characters repeat, return None."
# Example: 
# Input: "swiss" → Output: "w"
# Input: "aabb" → Output: None

def first_non_repeating_char(s):
    # Count character frequencies
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1

    # Find the first character with count = 1
    for char in s:
        if freq[char] == 1:
            return char
    return None


# --- Testing ---
print(first_non_repeating_char("swiss"))  # Expected "w"
print(first_non_repeating_char("aabb"))   # Expected None
print(first_non_repeating_char("abcab"))  # Expected "c"
print(first_non_repeating_char(""))       # Expected None


"""
Reflection (Timed Challenge) – ~230 words

For this timed challenge, I chose to use a dictionary to count character frequencies. 
Dictionaries provide O(1) average time for inserts and lookups, which made them the 
most efficient way to track occurrences of each character. Using a list would have 
required O(n) searches for each character, making the overall solution O(n^2). With 
a dictionary, the runtime is O(n), which is optimal for this problem.

The time limit shaped my decision by pushing me to go with a data structure that was 
straightforward and reliable. I knew that dictionaries are well-suited for counting, 
so I did not waste time considering more complex approaches. If I had more time, I 
might have added more robust error handling or experimented with an OrderedDict, but 
under the constraint, clarity and speed mattered more.

One compromise I made was keeping the solution simple rather than optimizing for 
memory. For very large strings, the dictionary could consume more space than 
necessary, but that trade-off is acceptable given the time pressure and the 
requirements of the problem. I also kept the testing light but targeted to cover 
basic and edge cases, like an empty string or all repeating characters.

Overall, the exercise taught me the importance of making quick, confident choices. 
It showed me that coding interviews are less about finding the most “clever” answer 
and more about delivering a correct, efficient solution within constraints.
"""
