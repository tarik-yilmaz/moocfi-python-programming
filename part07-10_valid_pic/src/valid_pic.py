# Write your solution here
from datetime import datetime

def is_it_valid(pic: str) -> bool:
    # If PIC is empty, return
    if len(pic) != 11:
        return False
    
    # Slice PIC to variables
    birthdate = pic[0:6]
    century_marker = pic[6]
    personal_identifier = pic[7:10]
    control_character = pic[10]

    
    if not birthdate.isdigit() or not personal_identifier.isdigit():
        return False
    
    if century_marker not in ["+", "-", "A"]:
        return False
    

    birth_day = birthdate[0:2]
    birth_month = birthdate[2:4]
    birth_year = birthdate[4:6]
    
    # Assign birthday year the correct century or return False
    if century_marker == "+":
        full_year = "18" + birth_year
    elif century_marker == "-":
        full_year = "19" + birth_year
    else:
        full_year = "20" + birth_year

    try:
        datetime(int(full_year), int(birth_month), int(birth_day))
    except ValueError:
        return False

    # Create control digit number and convert to integer
    control_digits = int(birthdate + personal_identifier)

    # Create the control string
    control_string = "0123456789ABCDEFHJKLMNPRSTUVWXY"

    # Divide by 31 and find the character at index of remainder
    control_character_at_index = control_string[control_digits % 31]

    if control_character_at_index != control_character.upper():
        return False

    return True

if __name__ == "__main__":
    is_it_valid("230827-906F")
    is_it_valid("120488+246L")
    is_it_valid("310823A9877")
    