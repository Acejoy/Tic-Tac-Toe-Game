'''
index is as follows:


       |       |        
    0  |   1   |   2    
_______|_______|________
       |       |        
    3  |   4   |   5    
_______|_______|________            
       |       |
    6  |   7   |   8
       |       |        



'''

import random


class Game:
    group_list = [[0,1,2],
                  [3,4,5],
                  [6,7,8],
                  [0,3,6],
                  [1,4,7],
                  [2,5,8],
                  [0,4,8],
                  [2,4,6]]

    def __init__(self):
        self.grid = [' ' for i in range(9)]
        
    def check_draw(self):

        draw = True
        for element in self.grid:
            if ' ' in element:
                draw = False
                break
        
        return draw

    def check_win(self, index):

        won = False
        win_char = ' '

        for group in Game.group_list:
            if index in group:

                character = self.grid[index]

                if self.grid[group[0]] == self.grid[group[1]] and\
                    self.grid[group[0]] == self.grid[group[2]]:
                    
                    win_char = character
                    won = True
                    break
        
        return (won, win_char)
                

    def display_grid(self):

        print()
        print('         |         |')
        print(f'    {self.grid[0]}    |    {self.grid[1]}    |    {self.grid[2]}')
        print('         |         |')
        print('_________|_________|_________')
        print('         |         |')
        print(f'    {self.grid[3]}    |    {self.grid[4]}    |    {self.grid[5]}')
        print('         |         |')
        print('_________|_________|_________')
        print('         |         |')
        print(f'    {self.grid[6]}    |    {self.grid[7]}    |    {self.grid[8]}')
        print('         |         |')
        
    
    def check_draw_or_win(self):
        # return break_out_of_while_loop:bool, character_won:string
        if self.check_draw():
            return (True, ' ')
        else:
            res = self.check_win()
            if res[0]:
                return (True, res[1])
            else:
                return (False, ' ')
        pass

    def play(self):
        
        indices_allowed = [i for i in range(9)]

        human_char = input('Choose X or O:').upper()
        if human_char not in ['X', 'O']:
            print('Invalid Symbol.')
            return
        
        computer_char = 'O' if human_char == 'X' else 'X'

        ## print the index to grid mapping
        print('\t0|1|2\n\t3|4|5\n\t6|7|8')
        
        # let first chance is human's
        # chance = 0 for human
        # chance = 1 for computer
        chance = 0
        symbols = {0:human_char, 1:computer_char}
        
        finale = ''

        ## only 9 inputs can be there so ,we run while loop and check for 9 inputs
        num_inputs = 0

        while num_inputs < 9:
            self.display_grid()    
            #print(indices_allowed)  

            ## computer's chance
            if chance == 1:
                index = random.choice(indices_allowed)
                self.grid[index] = symbols.get(chance)
                indices_allowed.remove(index)
                print(f'Computer inserted at index:{index}')
                chance = (chance+1)%2
                num_inputs +=1
                break_out_from_loop, character_won = self.check_win(index)

                if break_out_from_loop:                        
                        character_won = 'Human' if human_char == character_won else 'Computer'
                        finale = f'The game was won by:{character_won}'                    
                        break

            else:   

                index = input('Choose an index:')
                #index = int(index)
                
                if not index.isdigit():
                    print('Enter valid input.')
                elif int(index) not in indices_allowed:
                    print('Entered index is not allowed or not empty.')
                else:          
                    index = int(index)      
                    indices_allowed.remove(index)
                    self.grid[index] = symbols.get(chance)
                    chance = (chance+1)%2
                    num_inputs +=1
                    break_out_from_loop, character_won = self.check_win(index)

                    if break_out_from_loop:                    
                        character_won = 'Human' if human_char == character_won else 'Computer'
                        finale = f'The game was won by:{character_won}!!!'                    
                        break
                    
        self.display_grid()
        
        if self.check_draw():
            print('The game ended in Draw!!!')
        else:
            print(finale)
      
if __name__ == '__main__':
    game = Game()
    game.play()
