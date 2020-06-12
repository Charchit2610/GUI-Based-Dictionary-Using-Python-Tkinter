import json
from difflib import get_close_matches
data=json.load(open("data.json"))
def translate(w):
    w=w.lower()
   
    if w in data:
        return data[w]
    elif len(get_close_matches(w,data.keys()))>0:
        yn=input("Did you mean %s instead? Enter Y if yes or N if no"% get_close_matches(w,data.keys())[0])
        if yn=="Y":
            return data[get_close_matches(w,data.keys())[0]]
        elif yn=="N":
            return "The word doesn't exist.Please check it"
        else:
            return "we didn't understand your entry"
    else:
        return "The word doesn't exist"

word=input("Enter the word")
print(translate(word))
