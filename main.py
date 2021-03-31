import json , os
from difflib import get_close_matches

data = json.load(open('data.json'))

def clear():
    os.system('cls')


def word_meaning(w):
    return data.get(w)

def check_for_incorrect(word):
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()][0]
    elif word.upper() in data:
        return data[word.upper()][0]
    elif len(get_close_matches(word , data.keys() , cutoff=0.8)) > 0:
        most_matched = get_close_matches(word, data.keys())[0]
        clear()
        incorrect_input = input(f"Did You mean {most_matched} instead?, Press Y for yes and N for No ::- ").lower()
        if incorrect_input == 'y':
            return data[most_matched][0]
        elif incorrect_input == 'n':
            clear()
            return "The Word Doesn't Exist. Please Double Check it"
        else:
            clear()
            return "We didn't Understood your entry!!"
    else:
        clear()
        return "The Word Doesn't Exist. Please Double Check it"


if __name__ == "__main__":

    while True:
        word = input("Enter the word for it's meaning or 'X' for EXIT ::- ").lower()
        if word == 'x':
            break
        elif word_meaning(word) is not None:
            clear()
            print(word_meaning(word)[0])
        else:
            clear()
            print(check_for_incorrect(word))