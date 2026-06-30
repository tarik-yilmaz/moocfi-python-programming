# Write your solution here

def find_words(search_term: str) -> list:
    output_list = []

    with open("src/words.txt") as new_file:
        for line in new_file:
            line = line.replace("\n", "")

            # Search filter for `.` operator
            if "." in search_term:
                found = True
                if len(search_term) == len(line):
                    for index in range(len(search_term)):
                        if search_term[index] == ".":
                            continue
                        if search_term[index].lower() != line[index].lower():
                            found = False
                    if found:
                        output_list.append(line)

            # Search filter for words starting with "*"
            if search_term.startswith("*"):
                parts = search_term.split("*")

                if line.endswith(parts[1]):
                    output_list.append(line)
            
            # Search filter for words ending with "*"
            if search_term.endswith("*"):
                parts = search_term.split("*")

                if line.startswith(parts[0]):
                    output_list.append(line)

            # Search filter for words without wildcards
            if search_term == line:
                output_list.append(line)

    return output_list
