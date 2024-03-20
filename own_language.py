def split_command(command: str):
    return command.split(' ')


def run(program: list):
    output = []
    curr_location = 0

    variables = {
        'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0,
        'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0,
        'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0,
        'W': 0, 'X': 0, 'Y': 0, 'Z': 0
    }

    location_dict = {}
    for i in range(len(program)):
        if program[i].endswith(':'):
            location_dict[program[i][:len(program[i]) - 1]] = i

    while curr_location < len(program):
        curr_command = program[curr_location]
        curr_command_arr = split_command(curr_command)

        if curr_command_arr[0] == 'END':
            return output
        
        elif curr_command_arr[0] == 'PRINT':
            output.append(variables[curr_command_arr[1]] if curr_command_arr[1] in variables else int(curr_command_arr[1]))

        elif curr_command_arr[0] == 'MOV':
            if curr_command_arr[2] in variables:
                variables[curr_command_arr[1]] = variables[curr_command_arr[2]]
            else:
                variables[curr_command_arr[1]] = int(curr_command_arr[2])

        elif curr_command_arr[0] == 'ADD':
            if curr_command_arr[2] in variables:
                variables[curr_command_arr[1]] += variables[curr_command_arr[2]]
            else:
                variables[curr_command_arr[1]] += int(curr_command_arr[2])

        elif curr_command_arr[0] == 'SUB':
            if curr_command_arr[2] in variables:
                variables[curr_command_arr[1]] -= variables[curr_command_arr[2]]
            else:
                variables[curr_command_arr[1]] -= int(curr_command_arr[2])

        elif curr_command_arr[0] == 'MUL':
            if curr_command_arr[2] in variables:
                variables[curr_command_arr[1]] *= variables[curr_command_arr[2]]
            else:
                variables[curr_command_arr[1]] *= int(curr_command_arr[2])

        elif curr_command_arr[0] == 'JUMP':
            curr_location = location_dict[curr_command_arr[1]]
            continue

        elif curr_command_arr[0] == 'IF':
            sign = curr_command_arr[2]
            var1 = variables[curr_command_arr[1]]
            var2 = variables[curr_command_arr[3]] if curr_command_arr[3] in variables else int(curr_command_arr[3])

            if sign == '>=':
                if var1 >= var2:
                    curr_location = location_dict[curr_command_arr[5]]
                    continue
            elif sign == '<=':
                if var1 <= var2:
                    curr_location = location_dict[curr_command_arr[5]]
                    continue
            elif sign == '==':
                if var1 == var2:
                    curr_location = location_dict[curr_command_arr[5]]
                    continue
            elif sign == '!=':
                if var1 != var2:
                    curr_location = location_dict[curr_command_arr[5]]
                    continue
            elif sign == '<':
                if var1 < var2:
                    curr_location = location_dict[curr_command_arr[5]]
                    continue
            elif sign == '>':
                if var1 > var2:
                    curr_location = location_dict[curr_command_arr[5]]
                    continue
        
        curr_location += 1


    return output


# program4 = []
# program4.append("MOV N 50")
# program4.append("PRINT 2")
# program4.append("MOV A 3")
# program4.append("begin:")
# program4.append("MOV B 2")
# program4.append("MOV Z 0")
# program4.append("test:")
# program4.append("MOV C B")
# program4.append("new:")
# program4.append("IF C == A JUMP error")
# program4.append("IF C > A JUMP over")
# program4.append("ADD C B")
# program4.append("JUMP new")
# program4.append("error:")
# program4.append("MOV Z 1")
# program4.append("JUMP over2")
# program4.append("over:")
# program4.append("ADD B 1")
# program4.append("IF B < A JUMP test")
# program4.append("over2:")
# program4.append("IF Z == 1 JUMP over3")
# program4.append("PRINT A")
# program4.append("over3:")
# program4.append("ADD A 1")
# program4.append("IF A <= N JUMP begin")
# result = run(program4)
# print(result)
