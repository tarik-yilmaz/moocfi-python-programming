# Write your solution here

def search_by_name(filename: str, word: str) -> list:

    found_list = []

    with open(filename) as new_file:
        recipe_name = ""

        for line in new_file:
            line = line.replace("\n", "")

            if recipe_name == "":
                recipe_name = line

                if word.lower() in recipe_name.lower():
                    found_list.append(recipe_name)

            if line == "":
                recipe_name = ""

    return found_list
    

def search_by_time(filename: str, prep_time: int) -> list:
    
    recipe_list = []

    with open(filename) as new_file:
        recipe_name = ""

        for line in new_file:
            line = line.replace("\n", "")

            if recipe_name == "":
                recipe_name = line
                next_line_is_time = True
            
            elif next_line_is_time:
                time = int(line)

                if time <= prep_time:
                    recipe_list.append(f"{recipe_name}, preparation time {time} min")

                next_line_is_time = False

            if line == "":
                recipe_name = ""
        
    return recipe_list


def search_by_ingredient(filename: str, ingredient: str) -> list:
    found_list = []

    with open(filename) as new_file:
        
        recipe_name = ""

        for line in new_file:
            line = line.replace("\n", "")

            if recipe_name == "":
                recipe_name = line
                next_line_is_time = True
            
            elif next_line_is_time:
                time = int(line)
                next_line_is_time = False
            
            if ingredient.lower() == line.lower():
                found_list.append(f"{recipe_name}, preparation time {time} min")

            if line == "":
                recipe_name = ""

    return found_list