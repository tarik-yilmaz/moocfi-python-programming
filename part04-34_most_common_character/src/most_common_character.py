# Write your solution here

def most_common_character(text: str) -> str:
    common = text[0]

    for t in text:
        if text.count(t) > text.count(common):
            common = t

    return common
