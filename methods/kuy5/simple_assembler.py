from typing import Optional


def mov(args: list, all: Optional[list]):
    try:
        globals()[args[1]] = int(args[2])
    except ValueError:
        globals()[args[1]] = int(globals()[args[2]])
    globals()['result'].update({args[1]: int(globals()[args[1]])})


def inc(args: list, all: Optional[list]):
    globals()[args[1]] += 1
    globals()['result'].update({args[1]: int(globals()[args[1]])})


def dec(args: list, all: Optional[list]):
    globals()[args[1]] -= 1
    globals()['result'].update({args[1]: int(globals()[args[1]])})


def jnz(args: list, all: Optional[list]):
    op_index = all.index(args)

    if int(args[2]) < 0:
        while globals()[args[1]] > 0:
            for i in range(op_index + int(args[2]), op_index):
                globals()[all[i][0]](all[i], all)
    else:
        return int(args[2]) - 1


def simple_assembler(program):
    s = [i.split(' ') for i in program]
    globals()['result'] = {}
    step_skip: int = None

    for i in s:
        if step_skip is not None and not step_skip == 0:
            step_skip -= 1
            continue

        if i[1] not in globals():
            globals()[i[1]] = 0

        step_skip = globals()[i[0]](i, s)

    return globals()['result']
