import lyrics
def capitalize_each_word(original_str):
    result = ""
    # Split the string and get all words in a list
    list_of_words = original_str.split()
    # Iterate over all elements in list
    for elem in list_of_words:
        # capitalize first letter of each word and add to a string
        if len(result) > 0:
            result = result + " " + elem.strip().capitalize()
        else:
            result = elem.capitalize()
    # If result is still empty then return original string else returned capitalized.
    if not result:
        return original_str
    else:
        return result
sample_text = lyrics.x1
result = capitalize_each_word(sample_text)
f=open("cly.txt", "w")
f.write(result)
f.close()
print(result)
sample_text = lyrics.x2
result = capitalize_each_word(sample_text)
f=open("cly.txt", "a")
f.write(result)
f.close()
print(result)
sample_text = lyrics.x3
result = capitalize_each_word(sample_text)
f=open("cly.txt", "a")
f.write(result)
f.close()
print(result)
sample_text = lyrics.x4
result = capitalize_each_word(sample_text)
f=open("cly.txt", "a")
f.write(result)
f.close()
print(result)
