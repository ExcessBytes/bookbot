def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def word_count(filepath):
    text = get_book_text(filepath)
    words = text.split()
    count = len(words)
    return f"Found {count} total words"

from collections import Counter

def character_count(filepath):
    text = get_book_text(filepath).lower()
    counts = Counter(text)

    dictionary_list = [{"char": char, "num": count} for char, count in counts.items()]
    dictionary_list.sort(reverse=True, key=sort_on)
    
    return dictionary_list

def sort_on(items):
    return items["num"]    
        

 
 
            
            
            


