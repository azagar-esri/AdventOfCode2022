''' GOAL: Figure out crates and stacks '''

def interpret_stacks(file):
    stacks = []
    # Read input file
    while True:
        line = file.readline().rstrip('\n')
        line = line.replace("    "," ").replace("[","").replace("]","")
        if line.strip().split("   ")[-1].isdigit(): 
            file.readline() # empty line 
            break
        for idx, char in enumerate(line.split(" ")):
            if len(stacks) < (idx+1): 
                stacks.append([])
            if char != '': 
                stacks[idx].insert(0, char)
    return stacks

def part(file, part_num):
        
    stacks = interpret_stacks(file)
               
    # Rearrange crates 
    while True:
        line = file.readline().rstrip('\n')
        if not line: break
        instr = line.split(" ")
        num_moves, m_from, m_to = int(instr[1]), int(instr[3])-1, int(instr[5])-1
        if part_num == 1: # Part 1 method 
            for _ in range(num_moves):
                stacks[m_to].append(stacks[m_from].pop())
        elif part_num == 2: # Part 2 method
            to_len = len(stacks[m_to])
            for _ in range(num_moves):
                stacks[m_to].insert(to_len, stacks[m_from].pop())
    
    # Get crates at tops of stacks 
    tops = ""
    for stack in stacks:
        tops += stack[-1]
         
    print("Crates at tops of stacks: " + tops)

if __name__ == '__main__':
    
    input_file = 'Input/Day5.txt'
    with open(input_file) as file:
        part(file, 1)
    with open(input_file) as file:
        part(file, 2)