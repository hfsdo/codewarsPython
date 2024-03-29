def to_camel_case(text):
    first = True
    result = ""
    
    for word in text.replace("_", "-").split("-"):
        if first:
            result += word
            first = False
        else:
            result += word[:1].upper() + word[1:]

    return result