# Defining the Game class.
# It is made of rules, an initial state and a max_size(height,width)

class Game:
    def __init__(self, initial_state, rules, max_size):
        self.initial_state = initial_state
        self.rules = rules
        self.max_size = max_size
        
    def run_game(self, it):
        state = self.initial_state
        prev_state = None
        progression = []
        i = 0
        while (not state.equals(prev_state) and i < it):
            i += 1
            prev_state = state.copy()
            progression.append(previous_state.grid)
            state = state.apply_rules(self.rules, self.max_size)
        progression.append(state.grid)
        return progression