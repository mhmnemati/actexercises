def power_factorize(number, base):
    if (number % base != 0):
        return 0

    power = 0
    while (number % base == 0):
        base *= 2
        power += 1

    return power


def godel_decode(number):
    x = power_factorize(number + 1, 2)
    y = int((((number + 1) / 2 ** x) - 1) / 2)

    return (x, y)


def variable_encode(number):
    code = (number - 2) % 2
    index = int((number - 2) / 2) + 1

    if number == 1:
        return "Y"

    if code == 0:
        return f"X{index}"
    else:
        return f"Z{index}"


def label_encode(number):
    code = (number - 1) % 5
    index = int((number - 1) / 5) + 1

    if code == 0:
        return f"A{index}"
    elif code == 1:
        return f"B{index}"
    elif code == 2:
        return f"C{index}"
    elif code == 3:
        return f"D{index}"
    else:
        return f"E{index}"


def instruction_convert(number):
    (label, statement) = godel_decode(number)
    (code, variable) = godel_decode(statement)

    label = f"[{label_encode(label)}] " if label > 0 else ""
    variable = variable_encode(variable + 1)

    if code == 0:
        # X <- X
        return f"{label}{variable} <- {variable}"
    elif code == 1:
        # X <- X + 1
        return f"{label}{variable} <- {variable} + 1"
    elif code == 2:
        # X <- X - 1
        return f"{label}{variable} <- {variable} - 1"
    else:
        # IF X != 0 GOTO L
        return f"{label}IF {variable} != 0 GOTO {label_encode(code - 2)}"


print("\n".join(map(lambda x: instruction_convert(
    int(x)), input("Enter program: ").split(" "))))
