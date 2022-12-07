''' GOAL: Fix communications device '''

def part(file, part_num, sequence_num):
        
    # Read input file
    while True:
        line = file.readline().strip()
        if not line: break
        for i in range(0,len(line)-sequence_num):
            code = line[i:i+sequence_num]
            if len(set(code)) == sequence_num:
                print("Sequence marker part {0} ({1}): {2}".format(str(part_num), code, str(i+sequence_num)))
                break

if __name__ == '__main__':
    
    input_file = 'Input/Day6.txt'
    with open(input_file) as file:
        part(file, 1, 4)
    with open(input_file) as file:
        part(file, 2, 14)