''' GOAL: Calculate elf assignments '''

def part_1(file):
        
    # Hold total score
    total_pairs = 0
        
    # Read input file
    while True:
        line = file.readline().strip()
        if not line: break
        a_one = [int(x) for x in line.split(",")[0].split("-")]
        a_two = [int(x) for x in line.split(",")[1].split("-")]
        
        if (a_one[0] >= a_two[0] and a_one[1] <= a_two[1]) or (a_two[0] >= a_one[0] and a_two[1] <= a_one[1]):
            total_pairs += 1
            
    print("Total score part 1: " + str(total_pairs))
    
def part_2(file):
        
    # Hold total score
    total_pairs = 0
    
    # Read input file
    while True:
        line = file.readline().strip()
        if not line: break
        a_one = [int(x) for x in line.split(",")[0].split("-")]
        a_two = [int(x) for x in line.split(",")[1].split("-")]
        
        if not ((a_one[0] < a_two[0] and a_one[1] < a_two[0]) or (a_one[0] > a_two[1] and a_one[1] > a_two[1])):
            total_pairs += 1
       
    print("Total score part 2: " + str(total_pairs))

if __name__ == '__main__':
    
    input_file = 'Input/Day4.txt'
    with open(input_file) as file:
        part_1(file)
    with open(input_file) as file:
        part_2(file)