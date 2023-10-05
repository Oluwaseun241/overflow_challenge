def string_compression(string: str) -> str:
    compressed_string = ""
    count = 1
    # Iterate through the char
    for i in range(1, len(string)):
        if string[i] == string[i - 1]:
            count += 1
        else:
            compressed_string += string[i - 1] + str(count)
            count = 1 # Reset the count
    
    # Add the last char and its count
    compressed_string += string[-1] + str(count)

    # Check if the compressed string is shorter than the original
    if len(compressed_string) < len(string):
        return compressed_string
    else:
        return string

def main():
    string = "aaaabbbccddddddee"
    result = string_compression(string)
    print(result)

if __name__ == "__main__":
    main()

# Test cases
assert string_compression('bbcceeee') == 'b2c2e4'
assert string_compression('aaabbbcccaaa') == 'a3b3c3a3'
assert string_compression('a') == 'a'

# Explanation
# The time complexity of the algorithm here is O(n),
# where n is the length of input string
#
# Since the most significant factor in determining the time complexity
# is the loop that iterates through the input string, and it performs a 
# constant amount of work for each character, the overall time complexity 
# of the algorithm is O(n), where "n" is the length of the input string.

# This means that the algorithm's runtime grows linearly with the length of the input string.
