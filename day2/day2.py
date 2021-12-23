with open("input.txt") as f:
    instructions = f.read().splitlines()


# Part 1

depth, horizontal = 0, 0

for instruction in instructions:
    instruction_type, value = instruction.split(" ")
    value = int(value)

    if instruction_type == "down":
        depth += value
    elif instruction_type == "up":
        depth -= value
    elif instruction_type == "forward":
        horizontal += value

print(
    f"Your depth is {depth}, the horizontal position is {horizontal}, and multiplied that's {depth * horizontal}"
)


# Part 2

depth, horizontal, aim = 0, 0, 0

for instruction in instructions:
    instruction_type, value = instruction.split(" ")
    value = int(value)

    if instruction_type == "down":
        aim += value
    elif instruction_type == "up":
        aim -= value
    elif instruction_type == "forward":
        horizontal += value
        depth += value * aim


print(
    f"Your depth is {depth}, the horizontal position is {horizontal}, and multiplied that's {depth * horizontal}"
)
