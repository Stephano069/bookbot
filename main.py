def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        total_words = count_words(file_contents)
        char_dictionary = count_chars(file_contents)
        
        print("--- Begin report of books/frankenstein.txt ---\n")
        print(f"{total_words} words found in the document\n\n\n")
        for char in char_dictionary:
            if char.isalpha() != True:
                None
            else:
                print(f"The '{char}' character was found {char_dictionary[char]} times")
        print("--- End report ---")

def count_words(file_contents):
    result = len(file_contents.split())
    return result
    
def count_chars(file_contents):
    chars = {}
    lowercase_words = file_contents.lower()
    for word in lowercase_words:
        for char in word:
            if char in chars:
                break
            else:
                chars[char] = lowercase_words.count(char)

    sorted_by_values_dec = dict(sorted(chars.items(), key=lambda item: item[1], reverse=True))
    return sorted_by_values_dec

main()