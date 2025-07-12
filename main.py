import sys
for i in range(0, len(sys.argv), 1):
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

from stats import word_count

from stats import character_count



def main():
    word_count(sys.argv[1])
    sorted_list = character_count(sys.argv[1])
    for i in sorted_list:
        if i["char"].isalpha():
            print(f"{i['char']}: {i['num']}")
    return 
    
main()
