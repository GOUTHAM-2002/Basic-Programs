import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def dict(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input(
            "Did you mean %s instead, If yes enter 'Y' else enter 'N': "
            % get_close_matches(word, data.keys())[0]
        )
        if yn == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "N":
            return "This word doesn't exist"
        else:
            return "Please double check your entry"

    else:
        return "This word doesn't exist"


word = input("Enter words: ")

output = dict(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
