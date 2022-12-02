''' GOAL: Find elf with most calories '''


if __name__ == '__main__':
    # Store counts
    top_calories = []
    current_total = 0

    # Read input file
    with open('Input/Day1.txt') as f:
        while True:
            line = f.readline()
            if not line: break
            elif line == '\n':
                top_calories.append(current_total)
                current_total = 0
            else:
                current_total += int(line.strip())

    # Sort list and print answers
    top_calories.sort()
    print("Top 1 calories: " + str(top_calories[-1]))
    print("Top 3 calories sum: " + str(sum(top_calories[-3:])))