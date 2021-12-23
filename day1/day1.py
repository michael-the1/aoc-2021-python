with open("input.txt") as f:
    measurements = f.read().splitlines()

# Part 1

answer = sum(int(y) > int(x) for x, y in zip(measurements[:-1], measurements[1:]))
print(f"The answer to Day 1, part 1 is: {answer}")

# Part 2

answer = sum(int(y) > int(x) for x, y in zip(measurements[:-3], measurements[3:]))
print(f"The answer to Day 1, part 2 is: {answer}")
