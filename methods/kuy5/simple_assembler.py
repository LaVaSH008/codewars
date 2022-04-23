def simple_assembler(program):
    result = {}
    count = 0

    while count < len(program):
        command, var, attr = (program[count] + ' 0').split(' ')[:3]

        if command == 'inc':
            result[var] += 1

        if command == 'dec':
            result[var] -= 1

        if command == 'mov':
            if attr in result:
                result[var] = result[attr]
            else:
                result[var] = int(attr)

        if command == 'jnz':
            if var in result:
                if result[var]:
                    count += int(attr) - 1
            elif int(var):
                count += int(attr) - 1

        count += 1

    return result
