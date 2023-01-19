import re


def godel_encode(x, y):
    return (2 ** x) * (2 * y + 1) - 1


def variable_decode(name):
    if name == "Y":
        return 1

    if name[0] == 'X':
        return int(name[1:]) * 2
    else:
        return int(name[1:]) * 2 + 1


def label_decode(name):
    if name[0] == 'A':
        return int(name[1:]) * 5 - 4
    elif name[0] == 'B':
        return int(name[1:]) * 5 - 3
    elif name[0] == 'C':
        return int(name[1:]) * 5 - 2
    elif name[0] == 'D':
        return int(name[1:]) * 5 - 1
    else:
        return int(name[1:]) * 5


def instruction_convert(code):
    if "IF" in code:
        # IF X != 0 GOTO L
        groups = re.search("(\[([ABCDE]\d)\] )?IF ([XZ]\d|Y) != 0 GOTO ([ABCDE]\d)", code).groups()
        return godel_encode(
            label_decode(groups[1]) if groups[1] != None else 0,
            godel_encode(
                label_decode(groups[3]) + 2,
                variable_decode(groups[2]) - 1
            )
        )
    elif "+" in code:
        # X <- X + 1
        groups = re.search("(\[([ABCDE]\d)\] )?([XZ]\d|Y) <- ([XZ]\d|Y) \+ 1", code).groups()
        return godel_encode(
            label_decode(groups[1]) if groups[1] != None else 0,
            godel_encode(1, variable_decode(groups[2]) - 1)
        )
    elif "-" in code:
        # X <- X - 1
        groups = re.search("(\[([ABCDE]\d)\] )?([XZ]\d|Y) <- ([XZ]\d|Y) \- 1", code).groups()
        return godel_encode(
            label_decode(groups[1]) if groups[1] != None else 0,
            godel_encode(2, variable_decode(groups[2]) - 1)
        )
    else:
        # X <- X
        groups = re.search("(\[([ABCDE]\d)\] )?([XZ]\d|Y) <- ([XZ]\d|Y)", code).groups()
        return godel_encode(
            label_decode(groups[1]) if groups[1] != None else 0,
            godel_encode(0, variable_decode(groups[2]) - 1)
        )


# code = input("Enter instruction: ")
code = [
    "Z2 <- Z2 + 1",
    "[A1] IF X2 != 0 GOTO A2",
    "Z1 <- Z1 + 1",
    "Z1 <- Z1 + 1",
    "Z1 <- Z1 + 1",
    "IF Z2 != 0 GOTO B1",
    "[A2] X2 <- X2 - 1",
    "Z1 <- Z1 + 1",
    "Z1 <- Z1 + 1",
    "IF Z2 != 0 GOTO A1",
    "[B1] IF Z1 != 0 GOTO B2",
    "Y <- Y + 1",
    "IF Z2 != 0 GOTO E1",
    "[B2] IF X1 != 0 GOTO B3",
    "IF Z2 != 0 GOTO E1",
    "[B3] X1 <- X1 - 1",
    "Z1 <- Z1 - 1",
    "IF Z2 != 0 GOTO B1",
]

for line in code:
    print(instruction_convert(line))
