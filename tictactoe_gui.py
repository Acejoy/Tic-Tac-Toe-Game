import pygame
import random

bg_color = (0,221,176)
line_color = (0,166,133)
width = 600 +4
height = 600 +4

pygame.init()


class Game:
    group_list = [[0,1,2],
                  [3,4,5],
                  [6,7,8],
                  [0,3,6],
                  [1,4,7],
                  [2,5,8],
                  [0,4,8],
                  [2,4,6]]

    def __init__(self, human_char):
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption('Grid')
        self.screen.fill(bg_color)        
        
        self.nought_pic = pygame.image.load('pics/nought.png').convert_alpha()
        self.nought_pic = pygame.transform.smoothscale(self.nought_pic, (200, 200))
        self.cross_pic = pygame.image.load('pics/cross.png').convert_alpha()
        self.cross_pic = pygame.transform.smoothscale(self.cross_pic, (200, 200))
        

        # drawing lines
        pygame.draw.line(self.screen, line_color, (200, 0), (200, 600), width=2)
        pygame.draw.line(self.screen, line_color, (400, 0), (400, 600), width=2)
        pygame.draw.line(self.screen, line_color, (0, 200), (600, 200), width=2)
        pygame.draw.line(self.screen, line_color, (0, 400), (600, 400), width=2)

        pygame.display.flip()

        self.grid = [' ' for i in range(9)]
        self.indices_allowed = [i for i in range(9)]
        # chance=0 for human and chance=1 for computer
        self.chance = 0
        self.human_char = human_char
        self.computer_char = 'O' if human_char == 'X' else 'X'
        self.human_char_image = self.cross_pic if self.human_char =='X' else self.nought_pic
        self.computer_char_image = self.cross_pic if self.computer_char =='X' else self.nought_pic
        # print(self.human_char)
        # print(self.computer_char)

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
                
    def check_draw_or_win(self, index):
        # return break_out_of_while_loop:bool, character_won:string
        
        res = self.check_win(index)

        if res[0]:
            return res
        elif self.check_draw():
            return (True, ' ')
        else:
            return (False, ' ')

    
    def play_turn(self, index):              
        
        
            
        ## human's chance
        if index not in self.indices_allowed:
            print('Entered index is not allowed or not empty.')
            return False, ' '
        else:                            
            screen_x = (index%3)*202 
            screen_y = (index//3)*202
            self.indices_allowed.remove(index)
            self.grid[index] = self.human_char
            self.screen.blit(self.human_char_image, (screen_x, screen_y))
            pygame.display.flip()
            break_out_from_loop, character_won = self.check_draw_or_win(index)

            if break_out_from_loop:                    
                if character_won == ' ':
                    return (True, 'The game ended in Draw!!!')

                character_won = 'Human' if human_char == character_won else 'Computer'
                finale = f'The game was won by:{character_won}!!!'                    
                return (True, finale)


        ## computer's chance        
        index = random.choice(self.indices_allowed)
        self.grid[index] = self.computer_char
        screen_x = (index%3)*202 
        screen_y = (index//3)*202
        self.screen.blit(self.computer_char_image, (screen_x, screen_y))
        pygame.display.flip()
        self.indices_allowed.remove(index)

        # print(f'Computer inserted at index:{index}')
        
        break_out_from_loop, character_won = self.check_draw_or_win(index)

        if break_out_from_loop:                    
                if character_won == ' ':
                    return (True, 'The game ended in Draw!!!')

                character_won = 'Human' if human_char == character_won else 'Computer'
                finale = f'The game was won by:{character_won}!!!'                    
                return (True, finale)
        
        return False, ' '

    def mainloop(self):
        running = True
        solved = False

        while running:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    running  = False
                if not solved:

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        x, y = event.pos
                        index = (y//202)*3 +(x//202) 
                        solved, final_message = self.play_turn(index)
                        if solved:
                            print(final_message)


if __name__ == '__main__':
    
    human_char = input('Choose X or O:').upper()
    if human_char not in ['X', 'O']:
        print('Invalid Symbol.')
        exit()
    
    game = Game(human_char)
    game.mainloop()
    

