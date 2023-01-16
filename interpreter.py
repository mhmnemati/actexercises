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


def label_index(program, label):
    index = 0
    for instruction in program.split(" "):
        index += 1
        (ilabel, _) = godel_decode(int(instruction))
        if ilabel == label:
            return index

    return 0


def init_snapshot(program, inputs):
    inputs = inputs.split(" ")
    snapshot = {"i": 1, "Y": 0}

    for code in program.split(" "):
        (_, statement) = godel_decode(int(code))
        (_, variable) = godel_decode(statement)
        snapshot[variable_encode(variable + 1)] = 0

    xs = sorted([int(key[1:]) for key in snapshot.keys() if key[0] == 'X'])
    for i in range(1, xs[-1] if len(xs) > 0 else 0):
        snapshot[f"X{i}"] = int(inputs[i - 1]) if len(inputs) >= i else 0

    zs = sorted([int(key[1:]) for key in snapshot.keys() if key[0] == 'Z'])
    for i in range(1, zs[-1] if len(xs) > 0 else 0):
        snapshot[f"Z{i}"] = 0

    return snapshot


def successor_snapshot(program, snapshot):
    instruction = program.split(" ")[snapshot["i"] - 1]
    (_, statement) = godel_decode(int(instruction))
    (code, variable) = godel_decode(statement)

    variable = variable_encode(variable + 1)

    if code == 0:
        # X <- X
        snapshot["i"] += 1
        return snapshot
    elif code == 1:
        # X <- X + 1
        snapshot["i"] += 1
        snapshot[variable] = snapshot[variable] + 1
        return snapshot
    elif code == 2:
        # X <- X - 1
        snapshot["i"] += 1
        snapshot[variable] = snapshot[variable] - 1 if snapshot[variable] > 0 else 0
        return snapshot
    else:
        # IF X != 0 GOTO L
        next_i = label_index(program, code - 2)
        snapshot["i"] = next_i if snapshot[variable] > 0 else snapshot["i"] + 1
        return snapshot


def encode_snapshot(snapshot):
    i = snapshot["i"]
    Y = snapshot["Y"]
    xs = " ".join([str(snapshot[key]) for key in sorted([key for key in snapshot.keys() if key[0] == 'X'])])
    zs = " ".join([str(snapshot[key]) for key in sorted([key for key in snapshot.keys() if key[0] == 'Z'])])

    return f"{i} {xs} {zs} {Y}"


program = input("Enter program: ")
inputs = input("Enter inputs: ")

snapshot = init_snapshot(program, inputs)
while 0 < snapshot["i"] <= len(program.split(" ")):
    print(encode_snapshot(snapshot))
    snapshot = successor_snapshot(program, snapshot)
