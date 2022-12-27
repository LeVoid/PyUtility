"""
A class holding functions that may assist in handling text.
"""
__STRING_SEPARATOR = "\""

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
