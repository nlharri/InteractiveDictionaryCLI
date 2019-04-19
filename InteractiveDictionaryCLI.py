import json
import difflib

data = json.load(open("data.json"))

def translate(word):
    word_lower = word.lower()
    word_capital = word.capitalize()
    if word_lower in data:
        for definition in data[word_lower]:
            print("* {}".format(definition))
    elif word_capital in data:
        for definition in data[word_capital]:
            print("* {}".format(definition))
    else:
        close_matches = difflib.get_close_matches(word_lower, list(data.keys()), n=1, cutoff=0.8)
        if len(close_matches) > 0:
            accept_recommendation = input("Did you mean {} instead? (Type 'Y' or 'N') ".format(close_matches[0]))
            if accept_recommendation.lower() == 'y':
                for definition in data[close_matches[0]]:
                    print("* {}".format(definition))
            elif accept_recommendation.lower() == 'n':
                print("The word you entered doesn't exist. Please doublecheck it.")
            else:
                print("Wrong input.")
        else:
            close_matches = difflib.get_close_matches(word_capital, list(data.keys()), n=1, cutoff=0.8)
            if len(close_matches) > 0:
                accept_recommendation = input("Did you mean {} instead? (Type 'Y' or 'N') ".format(close_matches[0]))
                if accept_recommendation.lower() == 'y':
                    for definition in data[close_matches[0]]:
                        print("* {}".format(definition))
                elif accept_recommendation.lower() == 'n':
                    print("The word you entered doesn't exist. Please doublecheck it.")
                else:
                    print("Wrong input.")
            else:
                print("The word {} doesn't exist. Please doublecheck it.".format(word))

translate(input("Enter word: "))
