# Write your solution here

def no_vowels(text: str) -> str:
    vowels = ['a', 'e', 'i', 'o', 'u']

    for t in text:
        for v in vowels:
            if t == v:
                text = text.replace(t, "")

    return text