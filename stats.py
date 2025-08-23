from collections import Counter

def get_num_words(text:str):
    return len(text.split())

def letters_to_numbers (text: str) -> dict [str, int]:
    counts = {}
    for char in text.lower(): #only lower cases
        if char.isalpha(): #only letters
            counts [char] = counts.get(char, 0) +1
    return counts
    
    
    #letter_counts = {letter: text.count(letter) for letter in set(text) if letter != " "} 
    #return dict (Counter(text))

#def letter_list():
#    letter_counts = letters_to_numbers (text)
 #       for ch, n in sorted(letter_counts.items()):
  #          if ch.isalpha():
   #             return (f"'{ch}': {n}")







