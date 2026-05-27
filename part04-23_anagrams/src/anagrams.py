# Write your solution here

def anagrams(first_string: str, second_string: str) -> bool:
    if sorted(first_string) == sorted(second_string):
        return True
    
    return False

if __name__ == "__main__":
    anagrams()