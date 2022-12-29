"""
A class holding functions that may assist in handling text.
"""

__STRING_SEPARATOR : str = "\""
FUNCTIONS : list = [
    "tokenise",
    "listprint",
    "multi_input"
]

def help():
    listprint(FUNCTIONS, "Functions of TextHandler", "-> ")

def tokenise(input : str, separator : str = " ") -> list:
    """
    Turns the <input>-string into a list where every word is split by <separator>. If no separator is supplied, a whitespace is used.
    It also prevents cutting up strings inside of the input string, keeping them perfectly in tact.
    """
    splits = input.split(separator)
    final = []

    current_string = ""

    for spl in splits:
        if current_string != "":
            current_string += " " + spl.replace("\"", "")
            if "\"" in spl:
                final.append(current_string)
                current_string = ""
        elif "\"" in spl:
            current_string += spl.replace("\"", "")
        else:
            final.append(spl)

    if current_string != "":
        final.append(current_string)

    return final

def listprint(input : list, headline : str = "", prefix : str = "", suffix : str = "") -> None:
    """
    Prints every element in a list. A headline may be supplied, which is then printed above the list.
    If a prefix or suffix is supplied, it is printed before/after every item in the list respectively.
    """
    if headline != "":
        print(str(headline))

    for item in input:
        print(str(prefix) + str(item) + str(suffix))

def multi_input(questions : list) -> dict:
    """
    Takes a list of questions as an input and asks the user about every single one. The user is prompted to give an answer and the result is stored in a dictionary.
    The dictionary is returned at the end of the questions-list.
    """
    results : dict = {}

    for q in questions:
        results[q] = input(q + ": ")
    
    return results
