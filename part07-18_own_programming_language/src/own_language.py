# Write your solution here

# This exercise would be more challenging or tedius with input validation and
# error handling. Maybe later as an challenge?
# Or refactor it out like the model solution

def run(program: list) -> list:
    # Create dictionary with variables and set to zero
    variables = {
        "A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0, "G": 0, "H": 0, "I": 0, "J": 0,
        "K": 0, "L": 0, "M": 0, "N": 0, "O": 0, "P": 0, "Q": 0, "R": 0, "S": 0, "T": 0,
        "U": 0, "V": 0, "W": 0, "X": 0, "Y": 0, "Z": 0
    }

    # Create an index
    index = 0

    # Final output list
    output_list =  []
    
    while index < len(program):
        parts = program[index].split()

        if parts[0] == "PRINT":
            if parts[1].isdigit():
                output_list.append(int(parts[1]))
            else:    
                output_list.append(variables[parts[1]])
            index += 1

        elif parts[0] == "MOV":
            if parts[2].isdigit():
                variables[parts[1]] = int(parts[2])
            else:
                variables[parts[1]] = variables[parts[2]]
            index += 1

        elif parts[0] == "ADD":
            if parts[2].isdigit():
                variables[parts[1]] += int(parts[2])
            else:
                variables[parts[1]] += variables[parts[2]]
            index += 1

        elif parts[0] == "SUB":
            if parts[2].isdigit():
                variables[parts[1]] -= int(parts[2])
            else:
                variables[parts[1]] -= variables[parts[2]]
            index += 1

        elif parts[0] == "MUL":
            if parts[2].isdigit():
                variables[parts[1]] *= int(parts[2])
            else:
                variables[parts[1]] *= variables[parts[2]]
            index += 1

        # If command is a location just jump over it, we will get the index later through index() method
        elif len(parts) == 1 and parts[0] != "END":
            index += 1

        # Here, get the index from the program list consisting of  `:` char
        elif parts[0] == "JUMP":
            index = program.index(parts[1] + ":")

        elif parts[0] == "IF":
            jumped = False

            if parts[1].isdigit():
                condition1 = int(parts[1])
            else:
                condition1 = variables[parts[1]]

            if parts[3].isdigit():
                condition2 = int(parts[3])
            else:
                condition2 = variables[parts[3]]

            if parts[2] == "==":
                if condition1 == condition2:
                    index = program.index(parts[5] + ":")
                    jumped = True

            if parts[2] == "!=":
                if condition1 != condition2:
                    index = program.index(parts[5] + ":")
                    jumped = True

            if parts[2] == "<":
                if condition1 < condition2:
                    index = program.index(parts[5] + ":")
                    jumped = True

            if parts[2] == "<=":
                if condition1 <= condition2:
                    index = program.index(parts[5] + ":")
                    jumped = True

            if parts[2] == ">":
                if condition1 > condition2:
                    index = program.index(parts[5] + ":")
                    jumped = True

            if parts[2] == ">=":
                if condition1 >= condition2:
                    index = program.index(parts[5] + ":")
                    jumped = True

            if not jumped:
                index += 1

        elif parts[0] == "END":
            break

    return output_list

    
if __name__ == "__main__":
    # First Test [1, 2, 3]
    program1 = []
    program1.append("MOV A 1")
    program1.append("MOV B 2")
    program1.append("PRINT A")
    program1.append("PRINT B")
    program1.append("ADD A B")
    program1.append("PRINT A")
    program1.append("END")
    result = run(program1)
    print(result)

    # Example 2: [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]
    program2 = []
    program2.append("MOV A 1")
    program2.append("MOV B 10")
    program2.append("begin:")
    program2.append("IF A >= B JUMP quit")
    program2.append("PRINT A")
    program2.append("PRINT B")
    program2.append("ADD A 1")
    program2.append("SUB B 1")
    program2.append("JUMP begin")
    program2.append("quit:")
    program2.append("END")
    result = run(program2)
    print(result)

    # Example 3 (factorial): [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]
    program3 = []
    program3.append("MOV A 1")
    program3.append("MOV B 1")
    program3.append("begin:")
    program3.append("PRINT A")
    program3.append("ADD B 1")
    program3.append("MUL A B")
    program3.append("IF B <= 10 JUMP begin")
    program3.append("END")
    result = run(program3)
    print(result)

    # Example 4 (prime numbers): [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    program4 = []
    program4.append("MOV N 50")
    program4.append("PRINT 2")
    program4.append("MOV A 3")
    program4.append("begin:")
    program4.append("MOV B 2")
    program4.append("MOV Z 0")
    program4.append("test:")
    program4.append("MOV C B")
    program4.append("new:")
    program4.append("IF C == A JUMP error")
    program4.append("IF C > A JUMP over")
    program4.append("ADD C B")
    program4.append("JUMP new")
    program4.append("error:")
    program4.append("MOV Z 1")
    program4.append("JUMP over2")
    program4.append("over:")
    program4.append("ADD B 1")
    program4.append("IF B < A JUMP test")
    program4.append("over2:")
    program4.append("IF Z == 1 JUMP over3")
    program4.append("PRINT A")
    program4.append("over3:")
    program4.append("ADD A 1")
    program4.append("IF A <= N JUMP begin")
    result = run(program4)
    print(result)