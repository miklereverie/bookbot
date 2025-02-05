def main():
    path_to_file = "books/frankenstein.txt"
    def sort_on(dict):
      return dict["num"]
    
    def count_words(file_contents):
        with open(path_to_file) as f:
            file_contents = f.read()
        words = file_contents.split()
        wordsnum = len(words)
        return wordsnum
    
    def count_characters(file_contents):
        letterdict = {}
        letterlist= []
        with open(path_to_file) as f:
            file_contents = f.read()
        lowercase = file_contents.lower()
        for letter in lowercase:
            if letter not in letterdict:
                letterdict[letter] = 1
            else:
                letterdict[letter] += 1
        for letter in letterdict:
          if letter.isalpha() == True:
            letterlist.append({"character" : letter, "num" : letterdict[letter] })
        return letterlist
    
    
    words = count_words(path_to_file)
    characters = count_characters(path_to_file)
    sorted_characters = sorted(characters, key= lambda item:item["num"], reverse=True)
    
    print(f"--- Begin report of {path_to_file} ---")
    print(f"{words} words found in the document")
    for character in sorted_characters:
      print(f"The character '{character['character']}' was found {character['num']} times")
    print(f"--- End report ---")

main()
