import lyrics  # Import the 'lyrics' module that contains sample text

def capitalize_each_word(original_str):
    """
    Capitalizes the first letter of each word in the given string.
    
    Args:
    original_str (str): The input string to be capitalized.
    
    Returns:
    str: A string with each word's first letter capitalized.
    """
    result = ""
    # Split the string into a list of words
    list_of_words = original_str.split()
    
    # Iterate over each word in the list
    for elem in list_of_words:
        # Capitalize the first letter of the word and add it to the result string
        if len(result) > 0:
            result = result + " " + elem.strip().capitalize()
        else:
            result = elem.capitalize()
    
    return result

# List of sample texts from the 'lyrics' module
sample_texts = [lyrics.x1, lyrics.x2, lyrics.x3, lyrics.x4]

# Open the file in write mode to start fresh
with open("result.txt", "w") as file:
    for sample_text in sample_texts:
        # Capitalize each word in the sample text
        result = capitalize_each_word(sample_text)
        # Write the capitalized text to the file
        file.write(result + "\n")  # Add a newline for separation between texts
        # Print the result to the console
        print(result)
