import pyperclip
import string
from random import shuffle
import math
import random


class Password:
    def __init__(self):
        #actual settings
        self.leng = 0

        self.symbols = False

        self.numbers = False
        #characters used
        self.letters = list(string.ascii_letters)

        self.num = ['1','2','3','4','5','6','7','8','9','0']

        self.symb = ['!', '#', '$', '%', '^', '-', '*', '&', '@']

        #results

        self.entropy = 0 #bits

        self.guess_ps = 10**10 # guesses per second 

        self.brutetime = None

        self.password = ''

        
    def format_time(self, seconds):
        minute = 60
        hour = 3600
        day = 86400
        year = 31536000

        if seconds < minute:
            return f"{seconds:.2f} seconds"
        elif seconds < hour:
            return f"{seconds/minute:.2f} minutes"
        elif seconds < day:
            return f"{seconds/hour:.2f} hours"
        elif seconds < year:
            return f"{seconds/day:.2f} days"
        else:
            return f"{seconds/year:.2f} years"


    def settings(self):
        while True:
            try:
                self.leng = int(input('How many #s do you want: '))
                if self.leng < 8:
                    print('not enough characters')
                    continue

                while True:
                    symbol = input('do you want symbols (!@#$) Y or n: ')
                    if symbol == 'Y':
                        self.symbols = True
                        break
                    elif symbol == 'n':
                        break
                    else:
                        print('invalid input')

                
                while True:
                    numb = input('do you want numbers Y or n: ')
                    if numb == 'Y':
                        self.numbers = True
                        break
                    elif numb == 'n':
                        break
                    else:
                        print('invalid input')
                
                break

            except ValueError:
                print('Thats not a number')
                continue
    
    def make_nd_test (self):
        #creates entropy in bits
        character_set_size = 52
        if self.symbols == True:
            character_set_size += len(self.symb)
        if self.numbers == True:
            character_set_size += len(self.num)
        
        self.entropy = self.leng * math.log2(character_set_size)
        seconds = (2 ** (self.entropy - 1)) / self.guess_ps
        self.brutetime = self.format_time(seconds)


        #password creation
        while len(self.password) != self.leng:
            available_chars = self.letters.copy()
            if self.symbols:
                available_chars.extend(self.symb)
            if self.numbers:
                available_chars.extend(self.num)

            self.password = ''.join(random.choice(available_chars) for _ in range(self.leng))
    
    def results(self):
        print(f'Your password is {self.password}')
        print(f'It would take {self.brutetime} to brute force this password and the entropy is {self.entropy}')
        print('R: Restart, C: Copy to Clipboard')
        while True:
            final_options = input('do you want to R, C: ')
            if final_options == 'C':
                pyperclip.copy(self.password)
                print('Password copied to Clipboard')
                break
            elif final_options == 'R':
                break
            else:
                continue
        
    
#object
user = Password()

while True:
    create = input('Do you want to create a password(Y or n)? ')
    if create == 'Y':
        user.settings()
        user.make_nd_test()
        user.results()
    elif create == 'n':
        break
    else:
        print('incorrect input')