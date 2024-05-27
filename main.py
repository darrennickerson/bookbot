def main():
    book = "books/frankenstein.txt"

    with open(book) as f:
        file_contents = f.read()
        
    def count_words(source):
        words = source.split()
        return len(words)
    
    def count_letters(source):
        lowercase_letters = source.lower()
        
        list_of_chars = list(lowercase_letters)
        alpha_chars = set()
        char_dict = {}
        character_list = []
        
        for i in range(0, len(list_of_chars)):
            if list_of_chars[i].isalpha():
                alpha_chars.add(list_of_chars[i])
                
        for char in alpha_chars:
            char_dict[char] = 0
        
        for character in lowercase_letters:
            if character.isalpha():
                char_dict[character] += 1 
        for char_number in char_dict:
            new_dict = dict(character = char_number, number = char_dict[char_number])
            character_list.append(new_dict)
        
        return character_list
    
    def sort_on(dict):
        return dict["number"]
    
    end_list = count_letters(file_contents)

    end_list.sort(reverse=True, key=sort_on)

    number_of_words = count_words(file_contents)
    
    print(f"--- Begin report of {book} ---")
    print(f"{number_of_words} words found in the document")
    print()
    for character_num in end_list: 
        print(f"The {character_num["character"]} character was found {character_num["number"]} times")
    
    print("--- End Report ---")

main()