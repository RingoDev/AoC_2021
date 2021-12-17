with open("input.txt") as file:
    inputs = file.read().split("\n")
    split_inputs = []
    for number in inputs:
        x = [y for y in number]
        split_inputs.append(x)

    gamma_rate = []
    epsilon_rate = []
    for i in range(len(split_inputs[0])):
        count_0 = 0
        count_1 = 0
        for j in range(len(split_inputs)):
            if split_inputs[j][i] == "1":
                count_1 = count_1 + 1
            else:
                count_0 = count_0 + 1
        if count_1 == count_0:
            print("error same count")
        gamma_rate.append("0" if count_0 > count_1 else "1")
        epsilon_rate.append("1" if count_0 > count_1 else "0")

    gamma = int("".join(gamma_rate), 2)
    epsilon = int("".join(epsilon_rate), 2)

    print(f"power consumption: {gamma * epsilon}")


# part 2
def get_oxygen():
    with open("input.txt") as file:
        inputs = file.read().split("\n")
        split_inputs = []
        for number in inputs:
            x = [y for y in number]
            split_inputs.append(x)

        for i in range(len(split_inputs[0])):
            index_with_0 = []
            index_with_1 = []
            for j in range(len(split_inputs)):
                if split_inputs[j][i] == "0":
                    index_with_0.append(j)
                else:
                    index_with_1.append(j)
            # print(f"{i} : {len(index_with_0)}:{len(index_with_1)}")
            if len(index_with_0) > len(index_with_1):
                for index in sorted(index_with_1, reverse=True):
                    split_inputs.pop(index)
            else:
                for index in sorted(index_with_0, reverse=True):
                    split_inputs.pop(index)
            if len(split_inputs) == 1:
                return split_inputs[0]


def get_co2():
    with open("input.txt") as file:
        inputs = file.read().split("\n")
        split_inputs = []
        for number in inputs:
            x = [y for y in number]
            split_inputs.append(x)

        for i in range(len(split_inputs[0])):
            index_with_0 = []
            index_with_1 = []
            for j in range(len(split_inputs)):
                if split_inputs[j][i] == "0":
                    index_with_0.append(j)
                else:
                    index_with_1.append(j)
            # print(f"{i} : {len(index_with_0)}:{len(index_with_1)}")
            if len(index_with_0) > len(index_with_1):
                for index in sorted(index_with_0, reverse=True):
                    split_inputs.pop(index)
            else:
                for index in sorted(index_with_1, reverse=True):
                    split_inputs.pop(index)
            if len(split_inputs) == 1:
                return split_inputs[0]


oxygen = int("".join(get_oxygen()), 2)
co2 = int("".join(get_co2()), 2)
print(f"life support rating: {oxygen * co2}")
