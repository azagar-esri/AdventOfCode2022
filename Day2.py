''' GOAL: Calculate outcome of rock paper scissors strategy '''

class rps:
    
    shape_scoring = { 'X': 1, 'Y': 2, 'Z': 3 }
    
    def __init__(self, x, y=""):
        self.opponent_move = x
        self.your_move = y
        
    def calculate_your_move(self, outcome): 
        if (self.opponent_move == "A" and outcome == "Y") or (self.opponent_move == "B" and outcome == "X") or (self.opponent_move == "C" and outcome == "Z"):
            self.your_move = "X"
        elif (self.opponent_move == "A" and outcome == "Z") or (self.opponent_move == "B" and outcome == "Y") or (self.opponent_move == "C" and outcome == "X"):
            self.your_move = "Y"
        else: 
            self.your_move = "Z"
    
    def shape_score(self):
        return self.shape_scoring[self.your_move]
    
    def outcome_score(self):
        # rock > scissors, paper > rock, scissors > paper 
        if (self.your_move == 'X' and self.opponent_move == 'A') or (self.your_move == 'Y' and self.opponent_move == 'B') or (self.your_move == 'Z' and self.opponent_move == 'C'):
            return 3
        elif (self.your_move == 'X' and self.opponent_move == 'C') or (self.your_move == 'Y' and self.opponent_move == 'A') or (self.your_move == 'Z' and self.opponent_move == 'B'):
            return 6
        else:
            return 0
        
    def match_score(self):
        return self.shape_score() + self.outcome_score()

def part_1(file):
        
    # Hold total score
    total_score = 0
        
    # Read input file
    while True:
        line = file.readline()
        if not line: break
        moves = line.strip().split(" ")
        game = rps(moves[0], moves[1])
        total_score += game.match_score()
            
    print("Total score part 1: " + str(total_score))
    
def part_2(file):
        
    # Hold total score
    total_score = 0
        
    # Read input file
    while True:
        line = file.readline()
        if not line: break
        moves = line.strip().split(" ")
        game = rps(moves[0])
        game.calculate_your_move(moves[1])
        total_score += game.match_score()
            
    print("Total score part 2: " + str(total_score))

if __name__ == '__main__':
    
    input_file = 'Input/Day2.txt'
    with open(input_file) as file:
        part_1(file)
    with open(input_file) as file:
        part_2(file)