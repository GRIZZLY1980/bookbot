from stats import get_num_words, letters_to_numbers
import sys

def main ():
    if len(sys.argv) < 2:
        print ("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    filepath = sys.argv [1]
    text = read_file(filepath)

    text = read_file(filepath)
    
    num_words = get_num_words(text) #count words in text

    char_count = letters_to_numbers (text) #numbers count

    print_report(filepath, num_words, char_count)

def read_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def get_book_text(filepath):
    with open (filepath, "r") as f:
        file_contents = f.read ()
    return file_contents

def print_report(filepath, num_words, char_count):
    print ("============ BOOKBOT ============")
    print (f"Analyzing book found at {filepath}")
    print ("----------- Word Count ----------")
    print (f"Found {num_words} total words")
    print ("--------- Character Count -------")

    sorted_counts= sorted(
        char_count.items(), key = lambda item: item[1], reverse=True
    )

    for char, count in sorted_counts:
        print (f"{char}: {count}")

    print ("============= END ===============")

if __name__ == "__main__":
    main()