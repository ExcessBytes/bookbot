def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def word_count(filepath):
    text = get_book_text(filepath)
    word = text.split()
    count = 0
    for word in range(0,len(word), 1):
        count += 1
    print(f"Found {count} total words")

def character_count(filepath):
    text = get_book_text(filepath)
    lower_case_text = text.lower()
    dictionary = {}
    dictionary_list = []
    characters = list(lower_case_text)
    for i in characters:
        if i not in dictionary:
            dictionary[f"{i}"] = 0
        if i in dictionary:
            dictionary[f"{i}"] += 1
    for i in dictionary:
        dictionary_list.append({"char": i, "num": dictionary[i]})
        
    dictionary_list.sort(reverse=True, key=sort_on)
    return dictionary_list

def sort_on(items):
    return items["num"]    
        

 
 
            
            
            


