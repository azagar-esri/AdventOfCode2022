''' GOAL: Calculate rucksacks and badges '''

from itertools import zip_longest

def part_1(file):
        
    # Hold total score
    total_score = 0
        
    # Read input file
    while True:
        line = file.readline().strip()
        if not line: break
        mid = int(len(line)/2)
        first_compartment = set(line[:mid])
        second_compartment = set(line[mid:])
        overlap = [x for x in first_compartment if x in second_compartment][0]
        total_score += ord(overlap)-96 if ord(overlap)-96 > 0 else ord(overlap)-38
            
    print("Total score part 1: " + str(total_score))
    
def part_2(file):
        
    # Hold total score
    total_score = 0
    
    for next_n_lines in zip_longest(*[file] * 3):
        elf_group = [set(line.strip()) for line in next_n_lines]
        overlap = [x for x in elf_group[0] if x in elf_group[1] and x in elf_group[2]][0]
        total_score += ord(overlap)-96 if ord(overlap)-96 > 0 else ord(overlap)-38
       
    print("Total score part 2: " + str(total_score))

if __name__ == '__main__':
    
    input_file = 'Input/Day3.txt'
    with open(input_file) as file:
        part_1(file)
    with open(input_file) as file:
        part_2(file)