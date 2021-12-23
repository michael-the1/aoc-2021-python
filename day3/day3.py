def most_common_bit(s: str) -> str:
    return "1" if s.count("1") >= s.count("0") else "0"


def least_common_bit(s: str) -> str:
    return "0" if s.count("1") >= s.count("0") else "1"


def transpose(data: list[str]):
    return list(map(lambda x: "".join(x), zip(*data)))


with open("input.txt") as f:
    data = f.read().splitlines()


columns = transpose(data)
gamma_rate = "0b" + "".join(most_common_bit(col) for col in columns)
epsilon_rate = "0b" + "".join(least_common_bit(col) for col in columns)
power_consumption = int(gamma_rate, base=0) * int(epsilon_rate, base=0)

print(
    f"The gamma rate is {gamma_rate} and the epsilon rate is {epsilon_rate}. The power consumption is {power_consumption}."
)


def filter_candidates(data, i, bit_criteria_function):
    col = transpose(data)[i]
    bit_criteria = bit_criteria_function(col)
    candidates = [row for row in data if row[i] == bit_criteria]
    return candidates


def find_rating(data, bit_criteria_function):
    candidates = data
    i = 0
    while len(candidates) > 1:
        candidates = filter_candidates(candidates, i, bit_criteria_function)
        i = (i + 1) % len(data[0])
    rating = int("0b" + candidates[0], base=0)
    return rating


O2_rating = find_rating(data, most_common_bit)
CO2_rating = find_rating(data, least_common_bit)

print(
    f"The O2 rating is {O2_rating}, the CO2 rating is {CO2_rating}, multiplied that's {O2_rating * CO2_rating}"
)
