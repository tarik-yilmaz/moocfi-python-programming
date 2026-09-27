# WRITE YOUR SOLUTION HERE:

def filter_forbidden(string:str, forbidden: str) -> str:
    return "".join([s for s in string if s not in forbidden])


if __name__ == "__main__":
    sentence = "Once! upon, a time: there was a python!??!?!"
    filtered = filter_forbidden(sentence, "!?:,.")
    print(filtered)